#include<iostream>
#include<string.h>

using namespace std;

int main(int argc, char* argv[])
{
	char command[200];
	strcpy(command,"git add . & git commit -m \"");

	if(argc == 2){
		strcat(command,argv[1]);	
		strcat(command, "\" & git push origin master");
	    system(command);
	    cout << "\n\n Executing statement \n\n";
		cout << command;
	    cout << "\n\t Commited and Pushed ! \n";
	}
	else{
		cout << "\n\nEnter text to commit. \n\n";
		cout << "Something like this would work like a charm : <name of executable> \"<text for commit>\" \n\n" << endl;
	}

    return 1;
}