#!/bin/bash
openssl enc -e -des-ecb -nosalt -in file1 -out file1ecb.enc
openssl enc -e -des-cbc -nosalt -in file1 -out file1cbc.enc
openssl enc -e -des-cfb -nosalt -in file1 -out file1cfb.enc
openssl enc -e -des-ofb -nosalt -in file1 -out file1ofb.enc
openssl enc -e -des-ecb -nosalt -in file2 -out file2ecb.enc
openssl enc -e -des-cbc -nosalt -in file2 -out file2cbc.enc
openssl enc -e -des-cfb -nosalt -in file2 -out file2cfb.enc
openssl enc -e -des-ofb -nosalt -in file2 -out file2ofb.enc
openssl enc -e -des-ecb -nosalt -in file3 -out file3ecb.enc
openssl enc -e -des-cbc -nosalt -in file3 -out file3cbc.enc
openssl enc -e -des-cfb -nosalt -in file3 -out file3cfb.enc
openssl enc -e -des-ofb -nosalt -in file3 -out file3ofb.enc
