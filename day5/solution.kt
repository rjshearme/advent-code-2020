package main

import java.io.File
import java.io.InputStream
import java.lang.Math

class Seat(seatData: String) {
    val seatData = seatData
    val seatSplitPoint = 7

    fun calculateValue(): Int {
        val rowValue: Int = calculateRowValue(seatData)
        val colValue: Int = calculateColValue(seatData)
        val value = rowValue * 8 + colValue
        return value
    }

    fun calculateRowValue(seatData: String): Int {
        val rowData: String = seatData.substring(0, seatSplitPoint)
        val rowBoolList: List<Boolean> = rowData.map { char -> if (char=='B') true else false }
        return calculateValueFromBoolList(rowBoolList)
    }

    fun calculateColValue(seatData: String): Int {
        val colData: String = seatData.substring(seatSplitPoint)
        val colBoolList: List<Boolean> = colData.map { char -> if (char=='R') true else false }
        return calculateValueFromBoolList(colBoolList)
    }

    fun calculateValueFromBoolList(boolList: List<Boolean>): Int {
        var lowerLimit = 0.toDouble()
        var upperLimit = Math.pow(2.toDouble(), boolList.size.toDouble())
        boolList.forEach { bool ->
            var newLimit = (upperLimit + lowerLimit) / 2
            if (bool) {
                lowerLimit = Math.ceil(newLimit)
            } else {
                upperLimit = Math.floor(newLimit)
            }
        }
        return lowerLimit.toInt()
    }

}

class Solver {

    lateinit var stringData: String

    fun loadStringData(inputStringData: String) {
        this.stringData = inputStringData
    }

    fun solvePart1(): Int {
        val seatsData = extractSeats(this.stringData)
        val seatsValues = calculateSeatValues(seatsData)
        return calculateMaxSeatValue(seatsValues)
    }

    fun solvePart2(): Int {
        val seatsData = extractSeats(this.stringData)
        val seatsValues = calculateSeatValues(seatsData)
        return calculateMissingSeatId(seatsValues)
    }

    fun extractSeats(seatsData: String): List<Seat> {
        return seatsData.split("\n").map { seatDatum -> Seat(seatDatum) }
    }

    fun calculateSeatValues(seatData: List<Seat>): List<Int> {
        return seatData.map { seat -> seat.calculateValue() }
    }

    fun calculateMaxSeatValue(seatValues: List<Int>): Int {
        return seatValues.maxOrNull() ?: 0
    }

    fun calculateMissingSeatId(seatValues: List<Int>): Int {
        val seatsArray = seatValues.toIntArray()
        seatsArray.sort()
        var missingSeatId: Int = -1
        for (index in 0..seatsArray.size-3) {
            var firstId = seatsArray.get(index)
            var middleId = seatsArray.get(index+1).toDouble()
            var lastId = seatsArray.get(index+2)
            if ((firstId + middleId + lastId) / 3 != middleId) {
                missingSeatId = firstId + 1
            }
        }
        return missingSeatId
    }

}

fun main(args : Array<String>) {
    val inputString: String = args[0]
    val inputStream: InputStream = File(inputString).inputStream()
    val inputStringData = inputStream.bufferedReader().use { it.readText() }

    val solver = Solver()
    solver.loadStringData(inputStringData)
    val solution = solver.solvePart2()
    println(solution)
}

