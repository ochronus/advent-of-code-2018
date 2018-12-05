package ochronus.adventofcode_2018

import scala.io.Source
import scala.annotation.tailrec


object Day01 {
  def part1(): String = {
    val lines: Iterator[String] = Source.fromResource("day01.txt").getLines
    val changes = lines.takeWhile(_.nonEmpty).map(_.toInt)

    return changes.sum.toString
  }

  def part2(): String = {
    val lines: Iterator[String] = Source.fromResource("day01.txt").getLines
    val changes = lines.takeWhile(_.nonEmpty).map(_.toInt).toList

    @tailrec def visitFrequencies(changes: Stream[Int], currentFreq: Int, seenFreqs: Set[Int]): Int = {
      val nextFreq = currentFreq + changes.head
      if (seenFreqs contains nextFreq) nextFreq
      else visitFrequencies(changes.tail, nextFreq, seenFreqs + nextFreq)
    }

    val repeatingChanges = Stream.continually(changes.toStream).flatten
    return visitFrequencies(repeatingChanges, currentFreq = 0, seenFreqs = Set(0)).toString
  }

}
