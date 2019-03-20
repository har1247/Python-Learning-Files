/* Name          : Harpreet Singh
  * Student ID : 100287374
  * Description: This program performs the encryption steps of vigenere cipher and encrypt a file with a key of type String and make a new encrypted file. */
     
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cctype>
#include <string>

using namespace std;

/*convertToUpperCase function takes one parameter, string s, and converts lowercase letters to uppercase letters */
string convertToUpperCase(string s){
   for(unsigned int i=0; i<s.length(); i++){
      if(islower(s[i])) {
      s[i]=static_cast<char>('A'+(s[i]-'a'));
      }
   }
   return s;
}

/*keyPlacer function takes 2 parameters, string content and string k,  and returns string keyPlacer by placing key characters alternative to the file message characters  
  * Example- ATTACKATDAWN -> LEMONLEMONLE with key = LEMON*/
string keyPlacer(string content, string k) {
   string keyPlacer="";
   for(unsigned int i=0, j=0; i<content.length(); i++,j++){
      if(j>=k.length()){
         j=0;
      } 
      if(isdigit(content[i])) {
         keyPlacer+=" ";
      }
      keyPlacer+=k[j];
   }
 return keyPlacer;
}

/*shift function takes 2 parameters, string message and string key, and returns a string  that has encrypted message by shifting over message characters by key characters */
string shift(string message, string key){
   
   int c;
   string x="";

   for(unsigned int i=0; i<message.length(); i++)
   {
      if(isdigit(message[i])) {
         x+=message[i];
         continue;
      }
      
      c = (message[i] + key[i]) - 65 ;
      if(c>90) {
         c = (c-90) + 64;
      }
      x += static_cast<char>(c);
      
   }
      return x;
}   
  
/*encryptedFile function takes 2 parameters, string result, and string filename, and creates a new file with prefix 'e' and writes the encrypted message in it*/
void encryptedFile(string result, string fileName){
   ofstream out;
   out.open("e"+fileName+".txt");
   if(out.is_open()){
      out<<result<<endl;
   }
   out.close();
}

/*getMsg function takes one parameter, string filename, and returns a string message that has been fetch from a file*/
string getMsg(string filename){
   
   ifstream File;
   string line;
   string line2="";
  

   File.open(filename);
   
   if(File.is_open()){
      
      while(!File.eof()){
         File >> line;
         line2+=line;
      }
   }
      File.close();
      return line2;
}

/*getFile function takes one paramter, string filename, and returns the file name of the file that needs to be encrypted*/
string getFile(string filename){
   cout<<"Enter the file name thats need to be encrypted";
   cin>>filename;
   return filename;
}

/*getKey function takes one reference variable parameter, string &key, and ask the user to enter a key*/
void getKey(string &key){
   cout<<"Enter a key";
   cin>>key;
}

/*onlyAlphaNumeric function takes one paramter, string in, and returns the message that would be filter with only alphabets and digits. All other characters and symbols get discarded*/
string onlyAlphaNumeric(string in){
   string temp="";
   for(unsigned int i=0; i<in.length(); i++){
      if(isalpha(in[i]) || isdigit(in[i])){
         temp+= in[i];
      }
   }
   return temp;
}

/*main() is where program execution begins.*/
int main() {
   
      string key;
      string fileContent;
      string fileName;
     
      string keyContent;
      string keyGenerator;
      string encrypto;
      
      getKey(key);                                 //Calling getKey function to ask user to insert key.
      fileName = getFile(fileName);                //Calling getFile function to return the name of a file.
      fileContent=getMsg(fileName);                //Calling getMsg function to return message from the file.

      fileContent=convertToUpperCase(fileContent); //Calling convertToUpperCase function to convert lowercase to uppercase.
      key=convertToUpperCase(key);                 //Calling convertToUpperCase function to convert lowercase to uppercase.
      fileContent=onlyAlphaNumeric(fileContent);   //Calling onlyAlphaNumeric function to filter the message that ignores symbols.

      keyGenerator = keyPlacer(fileContent,key);   //Calling keyPlacer function to place key letters at their appropriate places.
      encrypto=shift(fileContent,keyGenerator);   //Calling shift function to encrypte the message.
      cout<<encrypto<<endl;
      encryptedFile(encrypto,fileName);            //Calling encryptedFile function to created encrypted file.
}
