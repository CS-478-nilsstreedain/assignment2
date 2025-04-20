#!/usr/bin/env python3
import sys
import pyshark

cap = pyshark.FileCapture(sys.argv[1])
flags = {'Telnet': False, 'FTP': False, 'SSL/TLS': False}
ports = set()
tls_bad = set()
creds = []
user = None

for p in cap:
    # 1. Telnet (simplest)
    if hasattr(p, 'telnet'):
        flags['Telnet'] = True

    # 2. FTP + credentials
    ftp = getattr(p, 'ftp', None)
    if ftp:
        flags['FTP'] = True
        cmd = getattr(ftp, 'request_command', '').lower()
        arg = getattr(ftp, 'request_arg', None)
        if cmd == 'user':
            user = arg
        elif cmd == 'pass' and user:
            creds.append(f"{user}:{arg}")
            user = None

    # 3. SSL/TLS + deprecated versions
    layer = getattr(p, 'tls', None) or getattr(p, 'ssl', None)
    if layer:
        flags['SSL/TLS'] = True
        ver = getattr(layer, 'handshake_version', None) or getattr(layer, 'record_version', None)
        if ver in ('0x0301', '0x0302'):
            tls_bad.add(ver)

    # 4. Port mismatch on TCP
    if p.transport_layer == 'TCP':
        src, dst = p.tcp.srcport, p.tcp.dstport
        for pr, svc in [('22','ssh'), ('80','http'), ('53','dns')]:
            if pr in (src, dst) and not hasattr(p, svc):
                ports.add(pr)

cap.close()

# Summary in order: Telnet, FTP, SSL/TLS
protocols = [name for name in ['Telnet', 'FTP', 'SSL/TLS'] if flags[name]]
print('Insecure protocols:', ', '.join(protocols) or 'None')
print('Port mismatches:', ', '.join(sorted(ports)) or 'None')
print('Deprecated TLS versions:', ', '.join(sorted(tls_bad)) or 'None')
print('FTP credentials:', ', '.join(creds) or 'None')
