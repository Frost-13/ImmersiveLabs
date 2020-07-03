#!/bin/bash
openssl enc -e -des-ecb -in file1 -out file1ecbsalted.enc
openssl enc -e -des-cbc -in file1 -out file1cbcsalted.enc
openssl enc -e -des-cfb -in file1 -out file1cfbsalted.enc
openssl enc -e -des-ofb -in file1 -out file1ofbsalted.enc
openssl enc -e -des-ecb -in file2 -out file2ecbsalted.enc
openssl enc -e -des-cbc -in file2 -out file2cbcsalted.enc
openssl enc -e -des-cfb -in file2 -out file2cfbsalted.enc
openssl enc -e -des-ofb -in file2 -out file2ofbsalted.enc
openssl enc -e -des-ecb -in file3 -out file3ecbsalted.enc
openssl enc -e -des-cbc -in file3 -out file3cbcsalted.enc
openssl enc -e -des-cfb -in file3 -out file3cfbsalted.enc
openssl enc -e -des-ofb -in file3 -out file3ofbsalted.enc
