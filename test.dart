import 'dart:io';
import 'dart:convert';

Future<List<List>> _main() async {
  String PRN = "1951721245049";
  // produces a request object
  var request = await HttpClient()
      .getUrl(Uri.parse('http://127.0.0.1:8000/getStudentAttendance/$PRN'));
// sends the request
  var response = await request.close();
// transforms and prints the response
  await for (var contents in response.transform(Utf8Decoder())) {
    String formattedContent = "";
    List<List> listSubKeyVal = [];

    int i = 0;
    for (i = 1; i < contents.length - 1; i++) {
      formattedContent += contents[i];
    }
    List<String> subjectKeyValue = formattedContent.split(",");
    for (i = 0; i < subjectKeyValue.length; i++) {
      listSubKeyVal.add(subjectKeyValue[i].toString().split(":"));
    }
    // print(listSubKeyVal);
    var subjectAttendances = [];
    var subjectNames = [];

    for (int i = 0; i < listSubKeyVal.length; i++) {
      subjectAttendances.add(listSubKeyVal[i][1]);
    }
    for (int i = 0; i < listSubKeyVal.length; i++) {
      subjectNames.add(listSubKeyVal[i][0]);
    }
    // print(subjectNames);
    // print(subjectAttendances);
    return listSubKeyVal;
  }
  return [];
}

void main(List<String> args) {
  Future<List<List>> out = _main();
}
