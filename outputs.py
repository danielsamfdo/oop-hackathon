CARE_PLAN_OUTPUT = """
Based on your MRI report, here are the possible treatment options for your lumbar spine issues:

- **No Treatment:** Since the facet arthropathy is within normal limits and there's no thecal sac compression, monitoring your condition might be sufficient if your pain is manageable.

- **Exercise and Physical Therapy:**
  - Level of Invasiveness: Noninvasive
  - Estimated Cost: Low to moderate
  - Potential Benefits: Improved mobility and pain reduction
  - Drawbacks: May initially cause some soreness

- **Superficial Heat:**
  - Level of Invasiveness: Noninvasive
  - Estimated Cost: Low (heating pads)
  - Potential Benefits: Moderate pain relief and improved function
  - Drawbacks: Temporary relief, potential for minor skin flushing

- **Massage Therapy:**
  - Level of Invasiveness: Noninvasive
  - Estimated Cost: Moderate
  - Potential Benefits: Small to moderate pain and function improvement
  - Drawbacks: Temporary relief, potential for muscle soreness

- **Acupuncture:**
  - Level of Invasiveness: Minimally invasive (needles)
  - Estimated Cost: Low to moderate
  - Potential Benefits: Small to moderate pain relief
  - Drawbacks: Temporary relief, potential discomfort from needles

- **Nonsteroidal Anti-inflammatory Drugs (NSAIDs):**
  - Level of Invasiveness: Noninvasive (medication)
  - Estimated Cost: Low
  - Potential Benefits: Small to moderate pain improvement
  - Drawbacks: Gastrointestinal and renal risks

- **Skeletal Muscle Relaxants (SMRs):**
  - Level of Invasiveness: Noninvasive (medication)
  - Estimated Cost: Low
  - Potential Benefits: Small pain relief
  - Drawbacks: Sedation, risk of central nervous system adverse effects

These treatment options can help manage your pain and improve your quality of life without significant invasiveness. Always discuss these options with your physician to tailor the best course of treatment based on your specific condition and preferences.
"""

DIAGNOSIS_OUTPUT = """
### Radiology Report Explanation for Regald, Regina

#### Patient Information
- **Name:** Regina Regald
- **Date of Birth:** 01/04/1967
- **Age:** 57 years
- **Gender:** Female
- **Referring Physician:** Dr. Ross Banner
- **Exam Date:** 01/01/2024
- **Exam Type:** MRI Lumbar Spine with and without contrast

#### Findings and Impressions

**Findings:**
- **Diffuse Degenerative Changes:** These changes are seen throughout Regina’s lumbar spine and are most pronounced at the L5-S1 disc level. This means that the wear and tear on the spinal discs is widespread, but particularly severe at one specific area.
- **Mild Disc Space Narrowing at L5-S1:** This refers to a decrease in the height of the space between the vertebrae where the disc is located, indicating some loss of disc substance.
- **Facet Arthropathy:** This is age-appropriate osteoarthritis of the small joints in the spine, which is normal for Regina’s age (57 years).
- **No Thecal Sac Compression:** The protective covering around the spinal cord and nerves is not being compressed, which is a good sign.
- **Normal Alignment:** The spine maintains its proper shape and alignment.

**Impressions:**
- **Degenerative Disc Disease, most prominent at L5-S1.**
- **Disc space narrowing at L5-S1.**
- **Diffuse facet arthrosis.**

#### Explanation
Regina, your MRI shows common signs of aging in the spine. Specifically, you have degenerative disc disease, especially at the L5-S1 level. This is quite common; studies show that around 88% of people your age have similar findings. The disc space narrowing and facet joint changes are also typical age-related changes. Importantly, there is no compression of the thecal sac, and your spine alignment is normal, which are positive findings.

#### Statistics
According to a systematic review, **88% of individuals aged 57 years** typically show signs of degenerative disc disease. These changes are often part of normal aging and may not necessarily cause pain or other symptoms.

#### Conclusion
While these findings indicate some degenerative changes, they align with what might be expected for someone of your age and may not be directly related to any symptoms you might have. It’s important to discuss these results with your doctor to determine the best course of action for any symptoms you are experiencing.

---

**Reference:**
Brinjikji et al., AJNR Am J Neuroradiol 2015, 36 (4) 811-816. DOI: [10.3174/ajnr.A4173](https://doi.org/10.3174/ajnr.A4173)
"""

PROVIDER_ASSISTANT_OUTPUT = """
Subject: Understanding Your Recent MRI Results and Next Steps

Dear Ms. Regald,

I hope this message finds you well. I wanted to take a moment to explain the findings of your recent MRI scan and discuss what steps we can take moving forward.

### MRI Results Summary
Your MRI of the lumbar spine shows the common signs of aging, particularly in the lower part of your spine (specifically, at the L5-S1 level). Here are the key points:
- **Degenerative Disc Disease** and **Disc Space Narrowing**: This means that the discs between your vertebrae are showing wear and tear, which is normal for people as they age.
- **Diffuse Facet Arthrosis**: The joints in your spine also show typical age-related changes.
- **Good News**: Your spine alignment is normal, and there is no compression on the spinal sac, which means no significant nerve pressure.

It's important to know that these changes are common. About 88% of people your age experience similar conditions, and these findings aren’t necessarily linked to pain.

### Treatment Options
You have several options to manage any symptoms you might be experiencing:

#### Non-Drug Treatments
1. **Superficial Heat**: Applying heat can help reduce pain and improve function.
2. **Massage**: This can offer short-term relief from discomfort.
3. **Acupuncture**: A technique that may help moderately improve pain.
4. **Exercise/Yoga/Tai Chi**: Engaging in these activities can help improve pain and functionality over time.
5. **Spinal Manipulation**: This can provide a potential small improvement in function.

#### Medications
1. **NSAIDs**: These are anti-inflammatory medications that can help reduce pain and inflammation.
2. **Skeletal Muscle Relaxants**: These can provide relief from pain but might cause drowsiness.

#### Additional Options if Needed
- **Tramadol or Duloxetine**: For moderate pain relief.
- **Opioids**: Only considered if other treatments fail due to potential risks, including addiction.

#### Observation
You might also choose to monitor your condition without active treatment as symptoms can improve over time.

### What's Next?
I'd like to discuss these options with you in more detail during our follow-up visit to find a treatment plan that fits your needs and preferences. Please let me know if you have any questions or concerns before then.

We are here to support you every step of the way. Your well-being is our priority, and we want to ensure you fully understand your condition and the available options.

Looking forward to seeing you soon.

Warm regards,

[Your Provider's Name]
[Your Clinic's Name]
[Contact Information]
"""