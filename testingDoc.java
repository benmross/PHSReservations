//Created 5/16/24 - Kimberly Crosier, Lead Tester
/* As of creation date, this java doc will be used to write all of our tests - formatting will be as follows:
   1) General plans and outlines for each test in a comment where each new test is numbered in order, explaining 
      what the test will test for, why I believed it was necessary to have a test for that, how important the test 
      is to the functionality of our website, etc.
   2) From the general outline comments of the test, JUnit testing code will be underneath, in the same format as 
      outlined in "testingInfo.java" (5/16 note: as of right now, I have plans to integrate the test via Maven - 
      there are other ways to run it via other Build Systems, IDE, or through command line, but I am just 
      experimenting as I am not intimately acquainted with all the possible ways Replit can run tests and which 
      would be easiest and least-time consuming for our project.
      TLDR: I am checking out Maven to see if we can run tests through that, if not, I'll try something else)

      //As of 5/17/24, Maven has been successfully downloaded
*/

/*
package com.example;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class AppTest {

  @Test
  public void shouldAnswerWithTrue() {
    assertTrue(true);
  }
}
*/

/*
1: Test Title Here 
     Level of importance of the test to the functionality of our website:
     What the test will test for:
     Why I think it is necessary to have a test for that:
     ------------
     //mvn clean compile test
     import staticorg.junit.Assert.assertEquals;
     import org.junit.*;
     public class ExampleTest{
       @Test
       public void testExampleMethod() throws Throwable {
         //Given
         Method underTest = new Method();

         //When
         double exampleVar = 80.0;
         String unit = "";
         double result = underTest.exampleMethod(exampleVar, unit);

         //Then - assertions for result of method exampleMethod(double, String)
         /*Note: format should be assertEquals(expected, actual, delta)
           where expected is defined expected outcome, actual is actual output return val, and
           delta is acceptable deviation between expected and actual val - specific to data validation
           meaning here we are validating a double val type, so delta should be a double too*/
     /*    assertEquals(176.0, result, 0.0);
       }
     }
*/
