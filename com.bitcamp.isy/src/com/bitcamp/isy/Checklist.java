package com.bitcamp.isy;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class Checklist {
	

	public static void main(String[] args) {
		Storage str1 = new Storage();		
		Student01 std = new Student01();
		Print print = new Print();
		Attendance01 atd = new Attendance01();
		
		ArrayList<Student> stdlist = std.input();//학생정보 입력 
		str1.setStdlist(stdlist);//학생정보 저장 
		print.Printstd(str1.getStdlist());// 학생정보 출력 
		ArrayList<Attendance> attlist = atd.input(str1.getStdlist());//출석정보 입력 
		str1.setAttlist(attlist);//출석정보 저장 
		print.Printatt(str1.getAttlist());//출석정보 출력 
		System.out.println();
		print.PrintAll(str1);//학생+출석정보 출력 
	
		
	}
	}

