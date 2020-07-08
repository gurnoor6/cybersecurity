## Solution/reference

### OpenSSL commands
https://www.sslshopper.com/article-most-common-openssl-commands.html

### Link relevant to this question
https://serverfault.com/questions/215606/how-do-i-view-the-details-of-a-digital-certificate-cer-file

### Exact command
`openssl x509 -inform der -in key.der -noout -text`
