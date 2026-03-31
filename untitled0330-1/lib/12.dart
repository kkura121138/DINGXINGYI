void main(){
  int num1=10;
  double pi=3.14;
  double num3=num1*pi;
  num num4=num1*pi;
  print("结果：");
  print("num1*pi(double类型)=$num3");
  print("num1*pi(num类型)=$num4");
}
void main(){
  String firstname='Gildong';
  String sirname='Hong';
  String fullname="$sirname $firstname";
  print("结果:");
  print("hello,$firstname");
  print("fullname : ${fullname.length}");
}
void main(){
  bool aa=false;
  bool bb=num1>0;
  bool chk=bb;
  print("结果：");
  print("check result is $chk");
}
void main(){
  int num1=10;
  double num2=3.141592;
  String num1Str=num1.toString();
  String num2Str=num2.toStringAsFixed(2);
  print("num1 to str is $num1Str");
  print("num2 to str is $num2Str");
}
void main(){
  int num1Parse=int.parse("-12");
  double num2Parse=double.parse("123.4567");
  num num3Parse=num.parse("-34.56");
  print(num1Parse);
  print(num2Parse);
  print(num3Parse);
}