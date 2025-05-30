# assignment2
## Learning Objective:

Select and Apply the best scanning techniques to perform reconnaissance on a specific network

This assignment allows you demonstrate your ability to utilize different scanning techniques and to articulate how you would determine which technique(s) to select.

## Setup:

For these exercises, I'm assuming you have at least 1 other device (smartphone, desktop, laptop, gaming system, etc.) connected to the same private network as your Kali Linux is connected to and that you know (or can look up) the private IP address of that other device. 

REMEMBER TO TARGET ONLY MACHINES/NETWORKS YOU ACTUALLY OWN!  (Or scanme.nmap.org as that server specifically allows for scanning.  Just don't try to exploit scanme.nmap.org as they don't allow that.)

**VM Notes:** if you are using a VM:

- If you are using a NAT network interface, you'll only be able see other VM's behind your Host OS's NAT, the Host OS's VM Network interface, and any other VM devices your VM might use.  That's perfectly fine.  Go ahead and adjust your expectations and narrative based on that... Just make sure you note this in your write up!
- If you're using Bridged, your VM might have some issues if you are using a wireless network.  Not all VMs play nice with bridged wireless.

**Cloud Notes:**  If you are using a Kali install in the cloud which doesn't have any local devices on its local cloud-based network:  

- Task 1 can work the same way.  You'll just probably be discovering that your cloud-based private network is very empty...(but maybe not as empty you would expect)
- Task 2 should work the same as written
- Tasks 3 and 4: In addition to having the Kali Linux scan itself, please also try scanning scanme.nmap.org
- If you feel really adventurous, you could create a VPN between your cloud-based Kali install and your local network and then scan your local network with your Kali install through the VPN.  This is probably more work than would be worth it for 1 week of activity.  But, if you have some spare time, learning how to do so is really interesting!

## Instructions:

You mission this week is to put on your penetration tester hat and find out as much information as you can about your target network via scanning.  At this stage we ARE NOT attempting to gain unauthorized access to the target network or devices.  We will be doing that later in the course and using a specific target server for that purpose.  For right now, we are just running the simple, non-invasive scans covered earlier in the module.

All write-up prompts should assume that your audience is the organization who hired you to perform the penetration test.  This means that your responses should be understandable by someone who may not be a technical person (think manager) and should also include enough technical depth for your response to be useful to the client's technical team(s).  The standard best-practice is to provide sections for "Executive Briefings" to summarize at a high level and "Technical Briefings" for the more in-depth technical discussion.

You are encouraged to use any of the tools covered in the prior explorations, but feel free to use any other non-invasive scanning tools.  If you aren't sure if a tool is invasive or not, please ask!

## Task 1:

Determine the number of active hosts on your local network using three (3) different techniques.  You must use a minimum of two (2) different tools (i.e. you cannot just use the same tool in three different ways).  Include screenshot demonstrations of each technique you selected showcasing how you were able to use the technique to identify the active hosts.

**Write-up prompts:**
- For each technique, explain the output and breakdown what information you were able to obtain by using the technique
- For each type of information obtained, explain how that information could reasonably be used by an attacker
- For each technique, explain what defenders might want to look for as an indication(s) they were being scanned
- Rank the techniques in order of how useful you feel they were in the situation, justify your ranking

## Task 2:

For each active host, attempt to perform OS fingerprinting using three (3) different techniques. You must use a minimum of two (2) different tools (i.e. you cannot just use the same tool in three different ways).  Include screenshot demonstrations of each technique you selected showcasing how you were able to use the technique to attempt to fingerprint the active hosts.  (NOTE: If a particular fingerprinting technique was unable to identify a host's OS, that is okay.  As long as you were properly applying the technique and its related tool(s), there will be no deduction if a VALID fingerprinting technique failed.)

**Write-up prompts:**
- For each technique, explain the output and breakdown what information you were able to obtain by using the technique
- For each type of information obtained, explain how that information could reasonably be used by an attacker
- For each technique, explain what defenders might want to look for as an indication(s) they were being scanned
- Rank the techniques in order of how useful you feel they were in the situation, justify your ranking

## Task 3:

For each active host, identify which ports are open using three (3) different techniques. You must use a minimum of two (2) different tools (i.e. you cannot just use the same tool in three different ways).  Record a demonstration of each technique you selected showcasing how you were able to use the technique to identify the open ports on each active host.

**Write-up prompts:**
- For each technique, explain the output and breakdown what information you were able to obtain by using the technique
- For each open port you identified, explain what that port is probably being used for (don't just name the protocol or service, explain what the protocol or service actually does)
- For each technique, explain what defenders might want to look for as an indication(s) they were being scanned
- Rank the techniques in order of how useful you feel they were in the situation, justify your ranking

## Task 4:

Identify AT LEAST five (5) services or protocols being used on the active hosts and indicate if those services are running at the current release level/version or not. If two (2) hosts are offering the same service/protocol and you find that the service/protocol is not current on both, those would count as two (2) services for this task.  You must use AT LEAST one (1) manual packet sniffing technique and AT LEAST (1) non-manual packet sniffing technique.  You DO NOT need to apply all of your techniques to all of the services/protocols for this task.  Record how you identified each of your services or protocols as being up-to-date or non-up-to-date.  (If your local network doesn't have at least 5 services and/or protocols being used, analyze the ones available and submit evidence showing that there aren't any other services/protocols.)  NOTES:  WSL won't be able to use most of the tools I highlighted for this task, so use the videos to explain how you WOULD use those tools. Some other network configurations may also run into issues with these tools.  That's fine, just explain how you would use them.

**Write-up prompts:**
- For each technique, explain the output and breakdown what information you were able to obtain by using the technique
- For each type of information obtained, explain how that information could reasonably be used by an attacker
- For each technique, explain what defenders might want to look for as an indication(s) they were being scanned
- Rank the techniques in order of how useful you feel they were in the situation, justify your ranking

## Grading Guidelines/Rubric:

30% of your grade is based on your application of your selected techniques.  70% of your grade is based on your write-up responses.

**Task Applications:**

IMPORTANT NOTE:  Mistakes made during your recordings which you also CORRECT during your recordings are NOT counted as deductions.  If you realize you performed a step out of order in your recording, you simply need to note that a given step was out of order and then perform the correct sequence of steps in your recording.  That way you do not need to start a new recording just because of a misstep.  Similarly, if you use the wrong option on a command, just re-run the command with the correct option and no deduction will occur (even if it takes you a few attempts to get the command options correct).

### Assignment Rubric

| | A – Level | B – Level | C – Level |
|---|---|---|---|
| **Task #1** | Was able to correctly apply each chosen technique and found all active hosts | Was able to apply each chosen technique, but may have performed a step out of order or incorrectly. Found all or most active hosts | Was able to apply each chosen technique, but may have performed multiple steps out of order or incorrectly. Found all or most active hosts |
| **Task #2** | Was able to correctly apply each chosen technique and correctly determine the OS of each active host by AT LEAST 1 technique | Was able to apply each chosen technique, but may have performed a step out of order or incorrectly. Correctly determined the OS of each (or most) active host by AT LEAST 1 technique | Was able to apply each chosen technique, but may have performed multiple steps out of order or incorrectly.  Correctly determined the OS of each (or most) active host by AT LEAST 1 technique |
| **Task #3** | Was able to correctly apply each chosen technique and found all open ports | Was able to apply each chosen technique, but may have performed a step out of order or incorrectly. Found all or most open ports | Was able to apply each chosen technique, but may have performed multiple steps out of order or incorrectly. Found all or most open ports |
| **Task #4** | Was able to correctly identify at least 5 services or protocols and determine if they were correctly up-to-date. Correctly applied at least 1 manual packet sniffing and 1 non-manual packet sniffing technique | Was able to correctly identify at least 4 services or protocols and determine if they were correctly up-to-date. Applied at least 1 manual packet sniffing and 1 non-manual packet sniffing technique, but may have performed a step out-of-order or incorrectly | Was able to correctly identify at least 3 services or protocols and determine if they were correctly up-to-date. Applied at least 1 manual packet sniffing and 1 non-manual packet sniffing technique, but may have performed multiple steps out-of-order or incorrectly |

**Write-up Evaluations:**

IMPORTANT NOTE:  For maximum points, make sure to format your write-up in a professional manner.  This means proper grammar, spelling, and use of headings.  As this is a 400/500 level course, those items are not specifically included in the rubric, but ARE expected of you in order to receive full credit.

### Evaluation Rubric

| | A – Level | B – Level | C – Level |
|---|---|---|---|
| **Prompt #1** | Complete breakdown of all information provided by each technique. Included appropriate output as part of breakdown. | Mostly complete breakdown of all information provided by each technique. May have left out a few types of information produced by the techniques. Included most of the appropriate output as part of breakdown. | Incomplete breakdown, but able to articulate the general themes/importance of the of all information provided by each technique. May have left out several types of information produced by the techniques. Included at least some relevant output as part of breakdown. |
| **Prompt #2** | All information covered. Each information type provided with a reasonable usage by an attacker. | Most information covered (AT LEAST 80% coverage) Covered information types provided with a reasonable usage by an attacker. | Most information covered (AT LEAST 70% coverage) Covered information types provided with a reasonable usage by an attacker. |
| **Prompt #3** | All techniques covered. Specific activities, indicators, or examples provided. Clear and accurate explanation for how the specified activities, indicators, or examples might reasonably be evidence of scanning | All or most techniques covered. Specific or general activities, indicators, or examples provided. Mostly clear and accurate explanation for how the provided activities, indicators, or examples might reasonably be evidence of scanning | All or most techniques covered. Specific or general or vague activities, indicators, or examples provided. Generally clear and accurate explanation for how the provided activities, indicators, or examples might reasonably be evidence of scanning |
| **Prompt #4** | Provided a complete ranking of techniques used. Justification for ranking for this specific network based on logic and evidence from the task | Provided a complete ranking of techniques used. Justification for ranking for this specific network mostly based on logic and evidence from the task | Provided a complete ranking of techniques used. Justification for ranking for this specific network has some basis in logic and evidence from the task |

## Deliverables:

A compressed folder (remember, the folder's name should be your username!) containing:

- A PDF containing your answers to the write-up prompts and your screenshots.  Please make sure to label your screenshots sufficiently so that your audience knows what each screenshot is supposed to show.
