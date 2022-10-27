# Description

Added the api to fetch patients' motion capture data from AWS S3
Added codes to store motion capture data into corresponding tables within the database

## Type of change

Please delete options that are not relevant.

- [√] Bug fix (non-breaking change which fixes an issue)
- [√] New feature (non-breaking change which adds functionality)

# How Has This Been Tested?

Please describe the tests that you ran to verify your changes. Provide instructions so we can reproduce. Please also list any relevant details for your test configuration

- [√] tests if the api that fetches motion capture data return desired output
- [√] tests if all queries to store data works well
- [√] test if the data are correctly stored in all corresponding tables


**Test Configuration**:
* Firmware version: N/A
* Hardware: N/A
* Toolchain: N/A
* SDK: N/A

# Checklist:

- [√] My code follows the style guidelines of this project
- [√] I have performed a self-review of my own code
- [√] I have commented my code, particularly in hard-to-understand areas
- [√] All my code explicity handle the error code for graceful error collection
- [ ] I have made corresponding changes to the documentation
- [√] My changes generate no new warnings
- [√] I have added tests that prove my fix is effective or that my feature works
- [√] New and existing unit tests pass locally with my changes
- [√] Any dependent changes have been merged and published in downstream modules