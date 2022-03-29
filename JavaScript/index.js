/*
//Percabangan
#1
var nilai = prompt("Inputkan nilai akhir:");
        var grade = "";

        if(nilai >= 90) grade = "A"
        else if(nilai >= 80) grade = "B+"
        else if(nilai >= 70) grade = "B"
        else if(nilai >= 60) grade = "C+"
        else if(nilai >= 50) grade = "C"
        else if(nilai >= 40) grade = "D"
        else if(nilai >= 30) grade = "E"
        else grade = "F";

        document.write(`<p>Grade anda: ${grade}</p>`);
#2

var nilai = prompt("Inputkan nilai akhir:");
    var grade = "";

    if (nilai >= 90){
        grade = "A"
    } else if(nilai >= 80) {
        grade = "B+"
    } else if(nilai >= 70) {
        grade = "B"
    } else if(nilai >= 60) {
        grade = "C+"
    } else if(nilai >= 50) {
        grade = "C"
    } else if(nilai >= 40) {
        grade = "D"
    } else if(nilai >= 30) {
         grade = "E"
    } else { 
        grade = "F";
    }
    document.write(`<p>Grade anda: ${grade}</p>`);

#3 SwitchCase
var nilai = prompt("input nilai");
var grade = "";

switch(true){
    case nilai < 90:
        grade = "A";
        break;
    case nilai < 80:
        grade = "B+";
        break;
    case nilai < 70:
        grade = "B";
        break;
    case nilai < 60:
        grade = "C+";
        break;
    case nilai < 50:
        grade = "C";
        break;
    case nilai < 40:
        grade = "D";
        break;
    case nilai < 30:
        grade = "E";
        break;
    default:
        grade = "F";
}

#4 Ternary
var jwb = prompt("Apakah Jakarta ibu kota indonesia?");

        var jawaban = (jwb.toUpperCase() == "IYA") ? "Benar": "Salah";

        document.write(`Jawaban anda: <b>${jawaban}</b>`);
#Nested
var username = prompt("Username:");
        var password = prompt("Password:");

        if(username == "petanikode"){
            if(password == "kopi"){
                document.write("<h2>Selamat datang pak bos!</h2>");
            } else {
                document.write("<p>Password salah, coba lagi!</p>");
            }
        } else {
            document.write("<p>Anda tidak terdaftar!</p>");
        }
###
var username = prompt("Username:");
var password = prompt("Password:");

if(username == "petanikode"){
    if(password == "kopi"){
        document.write("<h2>Selamat datang pak bos!</h2>");
    } else {
        document.write("<p>Password salah, coba lagi!</p>");
    }
} else {
    document.write("<p>Anda tidak terdaftar!</p>");
}

####
var username = prompt("Username:");
var password = prompt("Password:");

if(username == "petanikode" && password == "kopi"){
    document.write("<h2>Selamat datang pak bos!</h2>");
} else {
    document.write("<p>Password salah, coba lagi!</p>");
}

//perulangan
#for
#+
for(counter = 0; counter < 50; counter+=2){
    document.write("<p>Perulangan ke-"+counter+"</p>");
}
#-
for(counter = 10; counter > 0; counter--){
    document.write("<p>Perulangan ke "+counter+"</p>");
}

#While
var ulangi = confirm("Apakah anda mau mengulang?");
var counter = 0;

while(ulangi){
    counter++;
    ulangi = confirm("Apakah anda mau mengulang?");
}

document.write("Perulangan sudah dilakuakn sebanyak "+ counter +" kali");

#Do/While
var ulangi = confirm("Apakah anda mau mengulang?");;
var counter = 0;

do {
    counter++;
    ulangi = confirm("Apakah anda mau mengulang?");
} while(ulangi)

document.write("Perulangan sudah dilakuakn sebanyak "+ counter +" kali");

#Foreach
var languages = ["Javascript", "HTML", "CSS", "Typescript"];

for(i in languages){
    document.write(i+". "+ languages[i] + "<br/>");
}


var days = ["Senin", "Selasa", "Rabu", "Kamis", "Jum'at", "Sabtu", "Minggu"];
days.forEach((day) => {
    document.write("<p>" + day + "</p>");
});

#Repeat
#for
for( let i = 0; i < 100; i++){
    document.write("Ulangi kalimat ini!");
}

#repeat()
document.write("Ulangi kalimat ini! ".repeat(100));


###
*/
var ulangi = confirm("apakah anda ingin mengulang?");
var counter = 0;

while (ulangi) {
    counter++;
    var bintang = "*".repeat(counter) + "<br>";
    document.write(counter + ": " + bintang);
    ulangi = confirm("apakah anda ingin mengulang?");
}