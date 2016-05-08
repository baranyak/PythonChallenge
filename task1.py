import string

task_description = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq
glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

encrypted_url = "map"


def decrypt(encrypted_string):
    """
    In this function Caesar cipher with shift=2 is used
    :param encrypted_string: encrypted string with Caesar cipher
    :return: decrypted string
    """
    input_chars_table = string.ascii_lowercase
    output_chars_table = input_chars_table[2:] + input_chars_table[:2]
    return encrypted_string.translate(str.maketrans(input_chars_table, output_chars_table))


if __name__ == "__main__":
    print(decrypt(task_description))
    print(decrypt(encrypted_url))
