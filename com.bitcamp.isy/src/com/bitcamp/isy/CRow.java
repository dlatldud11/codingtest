package com.bitcamp.isy;

public class CRow {
private Student student;
private Attendance attendance;


public Student getStudent() {
	return student;
}
public void setStudent(Student student) {
	this.student = student;
}
public Attendance getAttendance() {
	return attendance;
}
public void setAttendance(Attendance attendance) {
	this.attendance = attendance;
}
@Override
public String toString() {
	// TODO Auto-generated method stub
	return student.getId()+"\t"+student.getName()+"\t"+student.getEmail()+"\t"+student.getPhonenumber()
	+"\t"+attendance.getMon()+"\t"+attendance.getTue()+"\t"+attendance.getWen()+"\t"+attendance.getThu()
	+"\t"+attendance.getFri()+"\t"+attendance.getSat()+"\t"+attendance.getSun();
}


}
