package com.bitcamp.isy;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class Attendance01 {
		
		public ArrayList<Attendance> input(ArrayList<Student> studentlist) {
		Scanner kb = new Scanner(System.in);
		ArrayList<Attendance> attendance = new ArrayList<Attendance>(); 
		
		for(int i=0; i<studentlist.size();++i) {
			Attendance att = new Attendance();
			att.setId(studentlist.get(i).getId());
			attendance.add(att);
		}
		
		for(int day=0; day<7; day++ ) {
			System.out.println("DAY" + day);
			String name = " ";
			do {
				System.out.println("이름 : ");
				name = kb.nextLine();
				for(Student st : studentlist) {
					if(st.getName().equals(name)) {
						for(Attendance at : attendance) {
							if(at.getId().equals(st.getId())) {
								String o = "출석";
								switch (day) {
									case 0:
										at.setMon(o);
										break;
									case 1:
										at.setTue(o);
										break;
									case 2:
										at.setWen(o);
										break;
									case 3:
										at.setThu(o);
										break;
									case 4:
										at.setFri(o);
										break;
									case 5:
										at.setSat(o);
										break;
									case 6:
										at.setSun(o);
										break;
								}
							}
						}
					}
				}
			}while(!name.equals("끝"));
		
		}kb.close();
		return attendance;
		}
}

