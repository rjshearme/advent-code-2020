package main

import (
  "fmt"
  "io/ioutil"
  "os"
  "regexp"
)

func main() {
  inputFile := os.Args[1]
  passports, err := loadpassport(inputFile)
  if err != nil {
    panic(err)
  }
  numValidPassports := countValidPassports(passports)
  fmt.Printf("There are %v valid passports in %v\n", numValidPassports, inputFile)
}

func loadpassport(inputFile string) (passports []string, err error) {
  data, err := loadStringData(inputFile)
  passportSplitExpr := regexp.MustCompile("\n\n")
  return passportSplitExpr.Split(data, -1), err
}

func loadStringData(inputFile string) (data string, err error) {
  raw_data, err := ioutil.ReadFile(inputFile)
  data = string(raw_data)
  return data, err
}

func countValidPassports(passports []string) (numValidPassports int) {
  numValidPassports = 0
  for i:=0; i < len(passports); i++ {
    if isValidPassport(passports[i]) {
      numValidPassports++
    }
    pidExpr := regexp.MustCompile("\\bpid:[0-9]{9}\\b")
    pid := pidExpr.FindString(passports[i])
    fmt.Println(pid, isValidPassport(passports[i]))
  }
  return numValidPassports
}

func isValidPassport(passport string) (isValid bool){
  hasBYR := PassportHasBYRField(passport)
  hasIYR := PassportHasIYRField(passport)
  hasEYR := PassportHasEYRField(passport)
  hasHGT := PassportHasHGTField(passport)
  hasHCL := PassportHasHCLField(passport)
  hasECL := PassportHasECLField(passport)
  hasPID := PassportHasPIDField(passport)

  return hasBYR && hasIYR && hasEYR && hasHGT && hasHCL && hasECL && hasPID
}

func PassportHasBYRField(passport string) (hasField bool) {
  byrExpr := regexp.MustCompile("\\bbyr:(19[2-9]\\d|200[012])\\b")
  return byrExpr.MatchString(passport)
}

func PassportHasEYRField(passport string) (hasField bool) {
  eyrExpr := regexp.MustCompile("\\beyr:20(2[0-9]|30)\\b")
  return eyrExpr.MatchString(passport)
}

func PassportHasIYRField(passport string) (hasField bool) {
  iyrExpr := regexp.MustCompile("\\biyr:20(1[0-9]|20)\\b")
  return iyrExpr.MatchString(passport)
}

func PassportHasHGTField(passport string) (hasField bool) {
  hgtExpr := regexp.MustCompile("\\bhgt:(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)\\b")
  return hgtExpr.MatchString(passport)
}

func PassportHasHCLField(passport string) (hasField bool) {
  hclExpr := regexp.MustCompile("\\bhcl:#[0-9a-f]{6}\\b")
  return hclExpr.MatchString(passport)
}

func PassportHasECLField(passport string) (hasField bool) {
  eclExpr := regexp.MustCompile("\\becl:(amb|blu|brn|gry|grn|hzl|oth)\\b")
  return eclExpr.MatchString(passport)
}

func PassportHasPIDField(passport string) (hasField bool) {
  pidExpr := regexp.MustCompile("\\bpid:[0-9]{9}\\b")
  return pidExpr.MatchString(passport)
}

