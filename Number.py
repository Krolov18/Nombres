# coding: utf-8

from Parser import Parser
from operator import mul, add
import typing


# class Number(Parser):
#     tokens = (
#         "UNIT",
#         "PLUS",
#         "TIMES",
#         "ZERO"
#     )
#
#     literals = ('(', ')', '+', '*')
#
#     # t_PLUS = r'\+'
#     # t_TIMES = r'\*'
#
#     @staticmethod
#     def t_UNIT(t):
#         r'\d+'
#         return t
#
#     @staticmethod
#     def t_ZERO(t):
#         r"""0"""
#         return t
#
#     @staticmethod
#     def t_newline(t):
#         r"""\n+"""
#         t.lexer.lineo += len(t.value)
#
#     t_ignore = ' \t'
#
#     @staticmethod
#     def t_error(t):
#         print('Je ne peux pas reconnaitre {0}'.format(t.value[0]))
#         t.lexer.skip(1)
#
#     def p_e_1(self, p):
#         """ E : E '+' T """
#         p[0] = [p[1], p[3]]
#
#     def p_e_2(self, p):
#         """ E : T """
#         p[0] = p[1]
#
#     def p_t_1(self, p):
#         """ T : T '*' F """
#         p[0] = [p[1], p[3]]
#
#     def p_t_2(self, p):
#         """ T : F """
#         p[0] = p[1]
#
#     def p_f_1(self, p):
#         """ F : '(' E ')' """
#         p[0] = p[2]
#
#     def p_f_2(self, p):
#         """ F : UNIT """
#         p[0] = p[1]
#
#     @staticmethod
#     def p_error(p):
#         print("Syntax error at '%s'" % p.value)


class Number(Parser):
    tokens = (
        "UNIT",
        "ZERO"
    )

    literals = ('(', ')', '*', '+')

    @staticmethod
    def t_UNIT(t):
        r"""(1|2|3|4|5|6|7|8|9)"""
        return t

    @staticmethod
    def t_ZERO(t):
        r"""0"""
        return t

    t_ignore = ' \t\n'

    @staticmethod
    def t_error(t):
        print('Je ne peux pas reconnaitre {0}'.format(t.value[0]))
        t.lexer.skip(1)

    def p_s_1(self, p):
        """
            S : T '+' unit
        """
        p[0] = reduire(p[1], int(p[3]), add, self.base)

    def p_s_2(self, p):
        """
            S : T '+' S
        """
        p[0] = reduire(p[1], p[3], add, self.base)

    @staticmethod
    def p_s_3(p):
        """
            S : '(' S ')'
        """
        p[0] = p[2]

    def p_t_1(self, p):
        """
            T : S '*' multi
        """
        p[0] = reduire(p[1], int(p[3]), mul, self.base)

    def p_t_2(self, p):
        """
            T : unit '*' multi
        """
        p[0] = reduire(int(p[1]), p[3], mul, self.base)

    @staticmethod
    def p_unit(p):
        """
            unit : UNIT
                 | ZERO
        """
        p[0] = p[1]

    @staticmethod
    def p_multi(p):
        """
            multi : UNIT zeros
        """
        p[0] = int("".join(p[1:]))

    @staticmethod
    def p_zeros(p):
        """
            zeros : ZERO
                  | ZERO zeros
        """
        import itertools
        if len(p) > 2:
            p[0] = "".join(list(itertools.chain(*[p[1]] + [p[2]])))
        else:
            p[0] = "".join(list(itertools.chain(*[p[1]])))

    @staticmethod
    def p_error(p):
        print("Syntax error at '%s'" % p.value)


def main():
    print(3)


if __name__ == '__main__':
    main()
