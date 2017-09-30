#include<iostream>

using namespace std;

int main()
{
        system("netsh interface ipv4 set address name=\"Wi-Fi\" source=dhcp");
        cout << "Attempting to switch to dynamic";
    return 0;
}