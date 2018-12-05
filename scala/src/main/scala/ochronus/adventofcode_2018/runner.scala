package ochronus.adventofcode_2018

import scala.reflect.runtime.universe


object Main extends App {
  if (args.length == 0) {
    Console.println("Gimme the day, f00l!")
    sys.exit(1)
  }

  var selectedDay = args(0)
  if (selectedDay.length() == 1) {
    selectedDay = s"0${selectedDay}"
  }

  val runtimeMirror = universe.runtimeMirror(getClass.getClassLoader)

  var module: runtimeMirror.universe.ModuleSymbol = null;

  try {
    module = runtimeMirror.staticModule(s"ochronus.adventofcode_2018.Day${selectedDay}")
  }
  catch {
    case _: Exception => {
      Console.println(s"No solutions for day #${selectedDay}")
      sys.exit(2)
    }
  }

  val im = runtimeMirror.reflectModule(module)
  val objMirror = runtimeMirror.reflect(im.instance)

  val method_part1 = im.symbol.info.decl(universe.TermName("part1")).asMethod
  val method_part2 = im.symbol.info.decl(universe.TermName("part2")).asMethod

  val result_part1 = objMirror.reflectMethod(method_part1)()
  val result_part2 = objMirror.reflectMethod(method_part2)()
  Console.println(s"Here are the solutions for day #${selectedDay}:")
  Console.println(s"Part 1: ${result_part1}")
  Console.println(s"Part 2: ${result_part2}")
}