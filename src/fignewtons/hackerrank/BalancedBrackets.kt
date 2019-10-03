package fignewtons.hackerrank


fun <E> ArrayList<E>.pop(): E =
    removeAt(size - 1)

fun isLeftBracket(bracket: Char): Boolean =
    bracket in setOf('(', '{', '[')

fun match(left: Char, right: Char): Boolean =
    when (left to right) {
        Pair('(', ')'), Pair('{', '}'), Pair('[', ']') -> true
        else -> false
    }

fun isBalanced(expr: String): Boolean {
    val stack = arrayListOf<Char>()
    for (bracket in expr) {
        if (isLeftBracket(bracket))
            stack.add(bracket)
        else if (stack.isEmpty() || !match(stack.pop(), bracket))
            return false
    }
    return stack.isEmpty()
}

fun main() {
    val pass = listOf("", "{}", "{}[]", "{[]}", "{{}}", "{{}{}}" )
    for (testCase in pass)
        println("$testCase - ${isBalanced(testCase)}")

    val fail = listOf("{", "}", "{[}]", "[{}")
    for (testCase in fail)
        println("$testCase - ${isBalanced(testCase)}")
}