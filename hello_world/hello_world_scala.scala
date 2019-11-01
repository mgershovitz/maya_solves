def printDiag(spaces: String, word: String): Unit = {
    if (!word.isEmpty) {
        Console.println(spaces + word.head)
        printDiag(spaces.concat(" "), word.tail)
    }
}

printDiag("", "Hello World!")