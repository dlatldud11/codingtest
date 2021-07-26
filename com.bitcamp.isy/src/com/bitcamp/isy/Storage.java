package com.bitcamp.isy;
import java.util.ArrayList;
import java.util.List;

public class Storage {
 ArrayList<Student> stdlist;
 ArrayList<Attendance> attlist;
 ArrayList<CRow> crowlist;
 

 public Storage() {
	 this.stdlist = new ArrayList<Student>();
	 this.attlist = new ArrayList<Attendance>();
	 this.crowlist = new ArrayList<CRow>();
	 
	 
 }
 public  ArrayList<Student> getStdlist() {
	return stdlist;
}
public void setStdlist(ArrayList<Student> stdlist) {
	this.stdlist = stdlist;
}
public  ArrayList<Attendance> getAttlist() {
	return attlist;
}
public void setAttlist(ArrayList<Attendance> attlist) {
	this.attlist = attlist;
}

public void AddStd(Student a) {
	this.stdlist.add(a);
}
 
public void AddAtt(Attendance attendance) {
	this.attlist.add(attendance);
}

public ArrayList<CRow> getCrowlist() {
	return crowlist;
}
public void setCrowlist(ArrayList<CRow> crowlist) {
	this.crowlist = crowlist;
}


}
