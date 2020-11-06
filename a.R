library(dplyr)
library(readxl)

setwd("D:/Dataset/")

exam_data <- "BDU_Digital_Analytics_Regression_Exam.xls"
open_file  <- file(exam_data, open = "r")
linecount <- 0
string_data <- ""
while (length(single_line <- readLines(open_file, n = 1, warn = FALSE)) > 0) {
  linecount <- linecount + 1
  if (linecount < 3) {
    exam_data <- paste0(exam_data,single_line)     
  }
  #Typical Google Analytics CSV outputs have the column headings in row 5
  if (linecount == 5) column_headings = strsplit(single_line, ",")[[1]]
  #We do not need the first 5 lines in the CSV
  if (linecount > 5) {
    #Typical Google Analytics CSV outputs have a blank row after the first data set
    if (gsub(pattern=",", x=single_line, replacement="") == "") break
    string_data <- paste0(string_data,single_line,"\n")
  }
}
close(open_file)
exam_table <- read.table(textConnection(string_data), sep=",", header=FALSE, stringsAsFactors = FALSE)
#Assigning the column headings to our data table
names(exam_table) <- column_headings


#Instead of the complex 'Week' column, let's add an ID column
exam_table$WeekID<-seq.int(nrow(exam_table))

