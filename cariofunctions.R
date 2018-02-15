localization <- function(chr,gstart,gend,png) { 

#This function creates an image with the localization of the retrotransposon in the chromosome were it's located. 
  
  library(crop)  #The crop library allows to crop the final image.
  library(karyoploteR) #Karyoploter generates the localization plot. 
  
  chrs <- toGRanges(   #TopGRanges collects the information about the localization (chromosome, starts and ends)
    data.frame(
      chr=chr, start= gstart,end= gend))
  
  png(filename = png, bg = "transparent", res = 120)  #png generates the png file. 

  kp <- plotKaryotype(genome="hg38", plot.type=4, chromosomes=chr) #plotKaryotype calls the genome that we are going to use. 
  kpAddBaseNumbers(kp) 
  kpDataBackground(kp, r0=0, r1=0.05, color = "gray77", data.panel = 2) 
  kpPlotRegions(kp, data=chrs, col="orchid4", r0=0, r1=0.1) #Makes the color block of the location of the retrotransposon. 

  dev.off.crop(file=png) #Closes the images and saves the file in the computer.

  return() #Since the image is saved in the computer, this function does not requiere a return. 
  
}

zoom <- function(chr,gstart,gend,png) {

#This function does basically the same thing that the previous one except that uses the parameter zoom in plotKaryotype to generate
#a zoom of the previous image. 
  
  zoom1 <- gstart - 10000000  #The range of the zoom
  zoom2 <- gend + 10000000    #The range of the zoom
  
  library(crop)
  library(karyoploteR)
  
  chrs <- toGRanges(
    data.frame(
      chr=chr, start= gstart,end= gend))
  
  detail.region <- toGRanges(data.frame(chr, zoom1, zoom2)) #Defines the variable that contains the information about the zoom.
  
  png(filename = png, bg = "transparent", res = 120)
  kp <- plotKaryotype(genome="hg38", plot.type=4, zoom = detail.region) #Calls the zoom variable. 
  kpAddBaseNumbers(kp, tick.dist=1000000)
  kpDataBackground(kp, r0=0, r1=0.05, color = "gray77", data.panel = 2)
  kpPlotRegions(kp, data=chrs, col="orchid4", r0=0, r1=0.1)
  dev.off.crop(file=png)
  return()
  
}





