# solution/references

## info in private key
https://crypto.stackexchange.com/questions/6593/what-data-is-saved-in-rsa-private-key

## viewing the key 
`openssl rsa -in keypair.pem -noout -text`

## CRT Parameters
According to wikipedia, these are stored for fast exponentiation on the recipient side.

