#!/bin/bash
openssl enc -d -des-ecb -in file1ecberrorsalted.enc -out decrypted_salt_error_files/file1ecberrorsalted_decrypted.txt
openssl enc -d -des-cbc -in file1cbcerrorsalted.enc -out decrypted_salt_error_files/file1cbcerrorsalted_decrypted.txt
openssl enc -d -des-cfb -in file1cfberrorsalted.enc -out decrypted_salt_error_files/file1cfberrorsalted_decrypted.txt
openssl enc -d -des-ofb -in file1ofberrorsalted.enc -out decrypted_salt_error_files/file1ofberrorsalted_decrypted.txt
openssl enc -d -des-ecb -in file2ecberrorsalted.enc -out decrypted_salt_error_files/file2ecberrorsalted_decrypted.txt
openssl enc -d -des-cbc -in file2cbcerrorsalted.enc -out decrypted_salt_error_files/file2cbcerrorsalted_decrypted.txt
openssl enc -d -des-cfb -in file2cfberrorsalted.enc -out decrypted_salt_error_files/file2cfberrorsalted_decrypted.txt
openssl enc -d -des-ofb -in file2ofberrorsalted.enc -out decrypted_salt_error_files/file2ofberrorsalted_decrypted.txt
openssl enc -d -des-ecb -in file3ecberrorsalted.enc -out decrypted_salt_error_files/file3ecberrorsalted_decrypted.txt
openssl enc -d -des-cbc -in file3cbcerrorsalted.enc -out decrypted_salt_error_files/file3cbcerrorsalted_decrypted.txt
openssl enc -d -des-cfb -in file3cfberrorsalted.enc -out decrypted_salt_error_files/file3cfberrorsalted_decrypted.txt
openssl enc -d -des-ofb -in file3ofberrorsalted.enc -out decrypted_salt_error_files/file3ofberrorsalted_decrypted.txt
