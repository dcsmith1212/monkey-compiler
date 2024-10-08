import unittest

from monkey.tokens import Token, TokenType
from monkey.lexer import Lexer

class LexerTestCase(unittest.TestCase):
   
    def test_next_token(self):

        input_string = '''
let five = 5;
let ten = 10;

let add = fn(x, y) {
x + y;
};

let result = add(five, ten);
!-/*5;
5 < 10 > 5;

if (5 < 10) {
    return true;
} else {
    return false;
}

10 == 10;
10 != 9;

"foobar"
"foo bar"

[1, 2, 3]
{"foo": "bar"}
'''
        expected_tokens = [
            Token(TokenType.LET, 'let'),
            Token(TokenType.IDENT, 'five'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.INT, '5'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.LET, 'let'),
            Token(TokenType.IDENT, 'ten'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.INT, '10'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.LET, 'let'),
            Token(TokenType.IDENT, 'add'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.FUNCTION, 'fn'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.IDENT, 'x'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.IDENT, 'y'),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.IDENT, 'x'),
            Token(TokenType.PLUS, '+'),
            Token(TokenType.IDENT, 'y'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.LET, 'let'),
            Token(TokenType.IDENT, 'result'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.IDENT, 'add'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.IDENT, 'five'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.IDENT, 'ten'),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.BANG, '!'),
            Token(TokenType.MINUS, '-'),
            Token(TokenType.SLASH, '/'),
            Token(TokenType.ASTERISK, '*'),
            Token(TokenType.INT, '5'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.INT, '5'),
            Token(TokenType.LT, '<'),
            Token(TokenType.INT, '10'),
            Token(TokenType.GT, '>'),
            Token(TokenType.INT, '5'),
            Token(TokenType.SEMICOLON, ';'),
		    Token(TokenType.IF, 'if'),
		    Token(TokenType.LPAREN, '('),
		    Token(TokenType.INT, '5'),
		    Token(TokenType.LT, '<'),
		    Token(TokenType.INT, '10'),
		    Token(TokenType.RPAREN, ')'),
		    Token(TokenType.LBRACE, '{'),
		    Token(TokenType.RETURN, 'return'),
		    Token(TokenType.TRUE, 'true'),
		    Token(TokenType.SEMICOLON, ';'),
		    Token(TokenType.RBRACE, '}'),
		    Token(TokenType.ELSE, 'else'),
		    Token(TokenType.LBRACE, '{'),
		    Token(TokenType.RETURN, 'return'),
		    Token(TokenType.FALSE, 'false'),
		    Token(TokenType.SEMICOLON, ';'),
		    Token(TokenType.RBRACE, '}'),
		    Token(TokenType.INT, '10'),
		    Token(TokenType.EQ, '=='),
		    Token(TokenType.INT, '10'),
		    Token(TokenType.SEMICOLON, ';'),
		    Token(TokenType.INT, '10'),
		    Token(TokenType.NOT_EQ, '!='),
		    Token(TokenType.INT, '9'),
		    Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.STRING, 'foobar'),
            Token(TokenType.STRING, 'foo bar'),
            Token(TokenType.LBRACKET, '['),
            Token(TokenType.INT, '1'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.INT, '2'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.INT, '3'),
            Token(TokenType.RBRACKET, ']'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.STRING, 'foo'),
            Token(TokenType.COLON, ':'),
            Token(TokenType.STRING, 'bar'),
            Token(TokenType.RBRACE, '}'),
		    Token(TokenType.EOF, '')
        ]


        l = Lexer(input_string)
        for expected_tok in expected_tokens:
            actual_tok = l.next_token()

            self.assertEqual(actual_tok.type, expected_tok.type)
            self.assertEqual(actual_tok.literal, expected_tok.literal)



if __name__ == '__main__':
    unittest.main(verbosity=2)