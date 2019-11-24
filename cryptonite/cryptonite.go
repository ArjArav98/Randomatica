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

	for i:=0; i<bits; i++ {

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

func main() {

	var bits int
	fmt.Scanf("%d", &bits)

	key := SymmetricKey(bits)
	fmt.Printf("%s\n", key);

}
