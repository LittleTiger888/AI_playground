c
#include <string.h>
#include <stdlib.h>

void CryptEncodeCombine(char *VarName, char *VarData, char *GlobalVar) {

	int Size;
	char *pEncoded;

	Size = (int)strlen(VarData);
	pEncoded = (char *)calloc(Size * 2, 1); //CUZ COMPRESSION IS DISABLED

	//crypt with xor
	_xor(VarData, Key, Size, (int)strlen(Key));

	//encode with base64
	base64_encode(VarData, Size, pEncoded, Size * 2);


	strcat(GlobalVar, VarName);
	strcat(GlobalVar, pEncoded);

	free(pEncoded);
}
