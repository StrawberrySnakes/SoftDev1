import caesar_cipher

def test_encrypt_letter_a():
    #setup
    letter = "A"
    shift = 3
    expected = "D"

    #invoke
    actual = caesar_cipher.encrypt_letter(letter, shift)

    #analyze
    assert actual == expected

def test_encrypt_letter_g():
    #setup
    letter = "G"
    shift = 5
    expected = "L"

    #invoke
    actual = caesar_cipher.encrypt_letter(letter, shift)

    #analyze
    assert actual == expected

def test_encrypt_letter_d():
    #setup
    letter = "D"
    shift = 10
    expected = "N"

    #invoke
    actual = caesar_cipher.encrypt_letter(letter, shift)

    #analyze
    assert actual == expected

def test_decrypt_letter_d():
    #setup
    letter = "d"
    shift = 3
    expected = "a"

    #invoke
    actual = caesar_cipher.decrypt_letter(letter, shift)

    #analyze
    assert actual == expected

def test_is_alphabetic_A():
    #setup
    character = "D"
    expected = True

    #invoke
    actual = caesar_cipher.is_alphabetic(character)

    #analyze
    assert actual == expected

def test_is_alphabetic_j():
    #setup
    character = "j"
    expected = False

    #invoke
    actual = caesar_cipher.is_alphabetic(character)

    #analyze
    assert actual == expected

def test_is_alphabetic_Z():
    #setup
    character = "V"
    expected = True

    #invoke
    actual = caesar_cipher.is_alphabetic(character)

    #analyze
    assert actual == expected

def test_is_alphabetic_Z():
    #setup
    character = "V"
    expected = True

    #invoke
    actual = caesar_cipher.is_alphabetic(character)

    #analyze
    assert actual == expected

def test_encrypt_message():
    #setup
    plaintext = "HELLO"
    shift = 4
    expected = "LIPPS"

    #invoke
    actual = caesar_cipher.encrypt_message(plaintext, shift)

    #analyze
    assert actual == expected

def test_decrypt_message():
    #setup
    ciphertext = "LIPPS"
    shift = 4
    expected = "HELLO"

    #invoke
    actual = caesar_cipher.decrypt_message(ciphertext, shift)

    #analyze
    assert actual == expected