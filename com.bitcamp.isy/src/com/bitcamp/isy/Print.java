package com.bitcamp.isy;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;




public class Print {

	public void Printstd(ArrayList<Student> studentlist) {	
		
		//인적 사항 출력하기 
				String[] title = {"순번", "이름", "이메일", "핸드폰"};
				for(int i=0; i<title.length; ++i) {
				System.out.print(title[i]+"\t");
				}
					System.out.println();

				for(Student s : studentlist) {
					String st = s.toString();
//					String out = String.join("\t", st);
					System.out.println(st);
					
					
		//인적 사항 출력하기 끝	
				}
	}
				
//public static void main(String[] args) {
	
 
		
//		List<Storage> rows = new ArrayList<Storage>();
//		ArrayList<Attendance> attlist = new ArrayList<Attendance>();


				public void Printatt(ArrayList<Attendance> attlist) {	
					//출결 사항 출력하기 
								String[] title2 = {"순번","월","화","수","목","금","토","일"};
								for(int i =0; i<title2.length; ++i){
									System.out.print(title2 [i]+"\t");
								}
									System.out.println();

							for(Attendance t: attlist) {
								String ar = t.toString();
								String out2 = String.join("\t", ar);
								System.out.println(out2);
							}
							}
					//출결 사항 출력하기 끝 
		
				public void PrintAll(Storage storage) {
// ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ인적 사항 + 출결 사항 
		ArrayList<Student> stdlist = storage.getStdlist();
		ArrayList<Attendance> attlist = storage.getAttlist();
		ArrayList<CRow> crowlist = storage.getCrowlist();
		
		String[] title3 = {"순번","이름","이메일","핸드폰","월","화","수","목","금","토","일"};
		for(int i =0; i<title3.length; ++i){
		System.out.print(title3 [i]+"\t");
		}
			System.out.println();
		
		for(Student a : stdlist) {
			for(Attendance b : attlist) {
				if( a.getId().equals(b.getId())) {
					CRow crow = new CRow();
					crow.setStudent(a);
					crow.setAttendance(b);
					crowlist.add(crow);
				}
			}
		}
		
			for(CRow a : crowlist) {
				 String ar = a.toString();
				 String out3 = String.join("\t", ar);
				 System.out.println(out3);
			   }
// ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ인적 사항 + 출결 사항 끝
				}
}
//}