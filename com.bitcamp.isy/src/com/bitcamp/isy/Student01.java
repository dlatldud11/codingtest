package com.bitcamp.isy;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Student01 {
	
	public ArrayList<Student> input() {
		
		
		int id = 1;
		Scanner kb = new Scanner(System.in);
		ArrayList<Student> stdlist = new ArrayList<Student>();
		
		for(int i =0; i < 3; i++) {
		Student student = new Student();
	    
		System.out.println("이름:");
		String a = kb.nextLine();
		student.setName(a);
		
		System.out.println("email");
		String b= kb.nextLine();
		student.setEmail(b);
		
		System.out.println("phonnumber");
		String c = kb.nextLine();
		student.setPhonenumber(c);
		
		student.setId(Integer.toString(id));
		++id;
		
		stdlist.add(student);
		
		}
		return stdlist;	
	}

}


