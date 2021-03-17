#!/bin/bash
openssl enc -d -des-ecb -nosalt -in file1ecberror.enc -out decrypted_nosalt_error_files/file1ecberror_decrypted.txt
openssl enc -d -des-cbc -nosalt -in file1cbcerror.enc -out decrypted_nosalt_error_files/file1cbcerror_decrypted.txt
openssl enc -d -des-cfb -nosalt -in file1cfberror.enc -out decrypted_nosalt_error_files/file1cfberror_decrypted.txt
openssl enc -d -des-ofb -nosalt -in file1ofberror.enc -out decrypted_nosalt_error_files/file1ofberror_decrypted.txt
openssl enc -d -des-ecb -nosalt -in file2ecberror.enc -out decrypted_nosalt_error_files/file2ecberror_decrypted.txt
openssl enc -d -des-cbc -nosalt -in file2cbcerror.enc -out decrypted_nosalt_error_files/file2cbcerror_decrypted.txt
openssl enc -d -des-cfb -nosalt -in file2cfberror.enc -out decrypted_nosalt_error_files/file2cfberror_decrypted.txt
openssl enc -d -des-ofb -nosalt -in file2ofberror.enc -out decrypted_nosalt_error_files/file2ofberror_decrypted.txt
openssl enc -d -des-ecb -nosalt -in file3ecberror.enc -out decrypted_nosalt_error_files/file3ecberror_decrypted.txt
openssl enc -d -des-cbc -nosalt -in file3cbcerror.enc -out decrypted_nosalt_error_files/file3cbcerror_decrypted.txt
openssl enc -d -des-cfb -nosalt -in file3cfberror.enc -out decrypted_nosalt_error_files/file3cfberror_decrypted.txt
openssl enc -d -des-ofb -nosalt -in file3ofberror.enc -out decrypted_nosalt_error_files/file3ofberror_decrypted.txt
