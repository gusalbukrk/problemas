#include <stdio.h>

int main(){
    int letras[26] = {0};
    int i, ans = 0;
    char p1[20], p2[20];
    scanf("%s", p1);
    scanf("%s", p2);
    for(i = 0; p1[i] != '\0'; i++){
        letras[p1[i]-97]++;
    }
    for(i = 0; p2[i] != '\0'; i++){
        letras[p2[i]-97]++;
    }
    for(i = 0; i < 26; i++){
        if(letras[i] > ans){
            ans = letras[i];
        }
    }
    if(ans < 3){
        printf("SIM\n");
    }else{
        printf("NAO\n");
    }
    return 0;
}