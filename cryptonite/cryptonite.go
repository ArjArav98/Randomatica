package main

import (
	"fmt"
	"time"
	"math/rand"
	"strings"
)

// Generates a private key for 
// symmetric-key cryptography.
func SymmetricKey(bits int) string {

	var key strings.Builder
	rand.Seed(int64(time.Now().Nanosecond()))

	for iter:=0; iter<bits; iter++ {

		chartype := rand.Int() % 3
		switch(chartype) {
			case 0:
				character := 'a' + byte(rand.Int()%26)
				key.WriteByte(character)
			case 1:
				character := 'A' + byte(rand.Int()%26)
				key.WriteByte(character)
			case 2:
				character := '0' + byte(rand.Int()%10)
				key.WriteByte(character)
		}

	}

	return key.String()

}

// Takes in the string and key and encrypts
// using a simple cesar cipher.
func CaesarEncrypt(text string, key string) string {

	keylen := len(key)
	textlen := len(text)

	var value byte
	var ciphertext strings.Builder

	switch(keylen>26) {
		case true: value = key[keylen%26]
		case false: value = key[26%keylen]
	}

	for iter:=0; iter<textlen; iter++ {
		ciphertext.WriteByte(text[iter]+value)
	}

	return ciphertext.String()

}

// Takes in the ciphertext and key and decrypts
// the caesar ciphertext.
func CaesarDecrypt(ciphertext string, key string) string {

	keylen := len(key)
	cipherlen := len(ciphertext)

	var value byte
	var text strings.Builder

	switch(keylen>26) {
		case true: value = key[keylen%26]
		case false: value = key[26%keylen]
	}

	for iter:=0; iter<cipherlen; iter++ {
		text.WriteByte(ciphertext[iter]-value)
	}

	return text.String()

}
