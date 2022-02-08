# libcardgen

**Library Card Generator**

When the pandemic hit, the public library where I work decided to start issuing library cards digitally so members of our community could access our online resources without first having to visit the building. Ordinarily the printing company that produces our physical library cards would do the work of generating library card numbers, so we needed to come up with our own way to generate card numbers that met our system's authentication requirements using a valid [checksum digit](https://en.wikipedia.org/wiki/Check_digit). The circulation department requested the numbers in an Excel spreadsheet.

I wrote this little program to run from the command line, generate the numbers, and save them in a spreadsheet.
