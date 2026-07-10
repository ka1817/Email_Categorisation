from src.model_prediction import ModelPrediction

predictor = ModelPrediction()

email = """
Hi KATTA PRANAV REDDY,

The three interview slots you had previously selected have now expired. But the good news is you can update your availability so we can schedule an interview at the earliest slot available.

To continue with the next steps in your recruitment journey, we kindly request you to share your updated availability at the earliest on the link below.
Please provide three preferred date and time options by submitting your availability through the following link:
Candidate Dashboard

You can also write to candidate.queries@accenture.com for any queries related to your interview.
We appreciate the effort you have invested in the process so far. Your interest and commitment are valued, and we look forward to supporting you as you move ahead in this opportunity.

At Accenture, all assessments and interview are recorded and go through multiple stages of auditing, both before and offer is extended and after onboarding.

We maintain stringent protocols to prevent any form of malpractice, including but not limited to cheating, unauthorized communication, the use of prohibited devices (such as mobile phones), and any attempts to tamper with systems, such as usage of malicious software.

Please ensure the following during your interview:
·   Keep your camera and microphone on throughout the interview.
·   Remain clearly visible in the camera for the duration of the interview.
·   Do not seek any external assistance or take help from others during the interview.

Any engagement in unauthorized or fraudulent activities, misrepresentation, or the use of unfair means during the recruitment process will lead to appropriate actions by Accenture. This may include disqualification from the current recruitment process as well as all future opportunities.

Your information, including answers, video, audio, and online session data, will be recorded, stored, viewed, and analyzed to ensure the integrity of the interview. Please be assured that this data will be handled in accordance with applicable data privacy laws and Accenture’s Global Privacy Statement as agreed upon during registration.

We encourage all candidates to adhere to these guidelines throughout assessments and interviews to ensure a fair and transparent process.

*Please take note that, unless there is a formal offer of employment from Accenture, any communication made by Accenture in respect of open position/selection process or steps related thereto shall not be assumed or treated to be as a commitment or an offer of employment or guarantee of employment with Accenture*

Good luck!

Thanks,
Accenture Recruitment Team
In case of any questions and concerns please reach out to 1-800-309-1147 and choose option 1 on IVR, Monday through Friday between 9:00 AM to 6:30 PM and You can also write to candidate.queries@accenture.com for any queries related to your interview. The turnaround time to receive an update will be within 2 business days.

<<Note: This is an auto-generated email, please do not reply to this email>>

Accenture is committed to keeping your personal data secure and processing it in accordance with applicable data protection laws. Read our privacy statement and the specific recruiting and hiring privacy statement, which include important information on why and how Accenture is processing your personal data.

Accenture has not authorized any agency, company or individual to either collect money or arrive on any monetary arrangement in exchange for a job at Accenture. Accenture's criterion for hiring candidates is merit. Any agency, company or individual offering employment with Accenture in exchange for money is misrepresenting their relationship with Accenture, which has not authorized any such action. If you are approached by any entity or individuals who demand money or any other form of compensation in return for a job offer at Accenture's even if they present themselves as representatives or employees of Accenture please send the details to our business ethics helpline. 



This message is for the designated recipient only and may contain privileged, proprietary, or otherwise confidential information. If you have received it in error, please notify the sender immediately and delete the original. Any other use of the e-mail by you is prohibited. Where allowed by local law, electronic communications with Accenture and its affiliates, including e-mail and instant messaging (including content), may be scanned by our systems for the purposes of information security, AI-powered support capabilities, and assessment of internal compliance with Accenture policy. Your privacy is important to us. Accenture uses your personal data only in compliance with data protection laws. For further information on how Accenture processes your personal data, please see our privacy statement at https://www.accenture.com/us-en/privacy-policy.
______________________________________________________________________________________

www.accenture.com
...

[Message clipped]  View entire message

"""

prediction = predictor.predict(email)

print(prediction)