#!/usr/bin/env python

# CAVEAT UTILITOR
#
# This file was automatically generated by TatSu.
#
#    https://pypi.python.org/pypi/tatsu/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.

from __future__ import annotations

import sys

from tatsu.buffering import Buffer
from tatsu.parsing import Parser
from tatsu.parsing import tatsumasu
from tatsu.parsing import leftrec, nomemo, isname # noqa
from tatsu.infos import ParserConfig
from tatsu.util import re, generic_main  # noqa


KEYWORDS = {}  # type: ignore


class fulling_motor_nameBuffer(Buffer):
    def __init__(self, text, /, config: ParserConfig = None, **settings):
        config = ParserConfig.new(
            config,
            owner=self,
            whitespace=None,
            nameguard=None,
            comments_re=None,
            eol_comments_re=None,
            ignorecase=False,
            namechars='',
            parseinfo=False,
        )
        config = config.replace(**settings)
        super().__init__(text, config=config)


class fulling_motor_nameParser(Parser):
    def __init__(self, /, config: ParserConfig = None, **settings):
        config = ParserConfig.new(
            config,
            owner=self,
            whitespace=None,
            nameguard=None,
            comments_re=None,
            eol_comments_re=None,
            ignorecase=False,
            namechars='',
            parseinfo=False,
            keywords=KEYWORDS,
        )
        config = config.replace(**settings)
        super().__init__(config=config)

    @tatsumasu()
    def _main_(self):  # noqa
        with self._optional():
            self._fl_()
        self._two_or_three_digit_number_()
        self.name_last_node('size')
        self._type_specific_()
        self.name_last_node('typed')
        self._define(
            ['size', 'typed'],
            []
        )

    @tatsumasu()
    def _gearbox_specifier_(self):  # noqa
        self._G_()
        self._float_number_()
        self.name_last_node('ratio')
        self._define(
            ['ratio'],
            []
        )

    @tatsumasu()
    def _type_specific_(self):  # noqa
        with self._choice():
            with self._option():
                self._stepper_t_()
                self.name_last_node('stepper')
                self._define(
                    ['stepper'],
                    []
                )
            with self._option():
                self._permanent_t_()
                self.name_last_node('permanent')
                self._define(
                    ['permanent'],
                    []
                )
            with self._option():
                self._brushless_t_()
                self.name_last_node('brushless')
                self._define(
                    ['brushless'],
                    []
                )
            with self._option():
                self._three_phase_t_()
                self.name_last_node('three_phase')
                self._define(
                    ['three_phase'],
                    []
                )
            self._error(
                'expecting one of: '
                '<brushless_marker> <brushless_t>'
                '<permanent_marker> <permanent_t>'
                '<price_performance_or_unknown_C_marker>'
                '<stepper_marker> <stepper_t>'
                '<three_phase_marker> <three_phase_t>'
            )
        self._define(
            ['brushless', 'permanent', 'stepper', 'three_phase'],
            []
        )

    @tatsumasu()
    def _three_phase_t_(self):  # noqa
        self._three_phase_marker_()
        self.name_last_node('type_marker')
        self._two_or_three_digit_number_()
        self.name_last_node('motor_body_length')
        self._three_phase_suffix_opt_our_()
        self.name_last_node('suffix')
        self._define(
            ['motor_body_length', 'suffix', 'type_marker'],
            []
        )

    @tatsumasu()
    def _three_phase_suffix_opt_our_(self):  # noqa
        with self._optional():
            self._three_phase_suffix_t_()

    @tatsumasu()
    def _three_phase_suffix_t_(self):  # noqa
        self._Dash_()
        self._two_digit_number_()
        self.name_last_node('current_per_phase_over_ten')
        self._two_digit_number_()
        self.name_last_node('leads')
        self._shafts_count_marker_opt_our_()
        self.name_last_node('shafts_count')
        self._define(
            ['current_per_phase_over_ten', 'leads', 'shafts_count'],
            []
        )

    @tatsumasu()
    def _stepper_suffix_t_(self):  # noqa
        self._Dash_()
        self._suffix_with_or_without_tail_()
        self.name_last_node('suffix_body')
        self._define(
            ['suffix_body'],
            []
        )

    @tatsumasu()
    def _suffix_with_or_without_tail_(self):  # noqa
        with self._choice():
            with self._option():
                self._suffix_with_current_()
                self.name_last_node('with_current')
                self._define(
                    ['with_current'],
                    []
                )
            with self._option():
                self._stepper_suffix_tail_()
                self.name_last_node('without_current')
                self._define(
                    ['without_current'],
                    []
                )
            self._error(
                'expecting one of: '
                '<digit> <stepper_suffix_tail>'
                '<suffix_with_current>'
                '<three_digit_number>'
            )
        self._define(
            ['with_current', 'without_current'],
            []
        )

    @tatsumasu()
    def _suffix_with_current_(self):  # noqa
        self._three_digit_number_()
        self.name_last_node('current')
        self._stepper_suffix_tail_()
        self.name_last_node('tail')
        self._define(
            ['current', 'tail'],
            []
        )

    @tatsumasu()
    def _double_step_rate_marker_(self):  # noqa
        with self._optional():
            self._M_()

    @tatsumasu()
    def _encoder_presence_marker_(self):  # noqa
        with self._optional():
            self._E_()

    @tatsumasu()
    def _unknown_marker_F_(self):  # noqa
        with self._optional():
            self._F_()

    @tatsumasu()
    def _keyway_marker_(self):  # noqa
        with self._optional():
            self._K_()

    @tatsumasu()
    def _screwed_shaft_marker_(self):  # noqa
        with self._optional():
            self._C_()

    @tatsumasu()
    def _gearbox_specifier_opt_our_(self):  # noqa
        with self._optional():
            self._gearbox_specifier_()

    @tatsumasu()
    def _hollow_specifier_opt_our_(self):  # noqa
        with self._optional():
            self._hollow_specifier_()

    @tatsumasu()
    def _shafts_count_marker_opt_our_(self):  # noqa
        with self._optional():
            self._shafts_count_marker_()

    @tatsumasu()
    def _shafts_count_and_step_rate_any_order_1_t_(self):  # noqa
        self._shafts_count_marker_opt_our_()
        self.name_last_node('shafts_count')
        self._double_step_rate_marker_()
        self.name_last_node('step_rate')
        self._define(
            ['shafts_count', 'step_rate'],
            []
        )

    @tatsumasu()
    def _shafts_count_and_step_rate_any_order_2_t_(self):  # noqa
        self._double_step_rate_marker_()
        self.name_last_node('step_rate')
        self._shafts_count_marker_opt_our_()
        self.name_last_node('shafts_count')
        self._define(
            ['shafts_count', 'step_rate'],
            []
        )

    @tatsumasu()
    def _shafts_count_and_step_rate_any_order_t_(self):  # noqa
        with self._choice():
            with self._option():
                self._shafts_count_and_step_rate_any_order_1_t_()
                self.name_last_node('shafts_count_and_step_rate_any_order_1')
                self._define(
                    ['shafts_count_and_step_rate_any_order_1'],
                    []
                )
            with self._option():
                self._shafts_count_and_step_rate_any_order_2_t_()
                self.name_last_node('shafts_count_and_step_rate_any_order_2')
                self._define(
                    ['shafts_count_and_step_rate_any_order_2'],
                    []
                )
            self._error(
                'expecting one of: '
                '<A> <B> <M> <double_step_rate_marker> <s'
                'hafts_count_and_step_rate_any_order_1_t>'
                '<shafts_count_and_step_rate_any_order_2_'
                't> <shafts_count_marker>'
                '<shafts_count_marker_opt_our>'
            )
        self._define(
            ['shafts_count_and_step_rate_any_order_1', 'shafts_count_and_step_rate_any_order_2'],
            []
        )

    @tatsumasu()
    def _stepper_suffix_tail_(self):  # noqa
        self._digit_()
        self.name_last_node('variant')
        self._shafts_count_and_step_rate_any_order_t_()
        self.name_last_node('shafts_count_and_step_rate_any_order')
        self._encoder_presence_marker_()
        self.name_last_node('encoder')
        self._unknown_marker_F_()
        self.name_last_node('unknown_F')
        self._keyway_marker_()
        self.name_last_node('key_way')
        self._screwed_shaft_marker_()
        self.name_last_node('screwed_shaft')
        self._gearbox_specifier_opt_our_()
        self.name_last_node('gearbox')
        self._hollow_specifier_opt_our_()
        self.name_last_node('hollow')
        self._define(
            ['encoder', 'gearbox', 'hollow', 'key_way', 'screwed_shaft', 'shafts_count_and_step_rate_any_order', 'unknown_F', 'variant'],
            []
        )

    @tatsumasu()
    def _stepper_modifiers_opt_our_(self):  # noqa
        with self._optional():
            self._stepper_modifiers_t_()

    @tatsumasu()
    def _stepper_t_(self):  # noqa
        self._stepper_marker_()
        self.name_last_node('type_marker')
        self._stepper_modifiers_opt_our_()
        self.name_last_node('stepper_modifiers')
        self._two_or_three_digit_number_()
        self.name_last_node('motor_body_length')
        self._stepper_suffix_t_()
        self.name_last_node('suffix')
        self._define(
            ['motor_body_length', 'stepper_modifiers', 'suffix', 'type_marker'],
            []
        )

    @tatsumasu()
    def _stepper_series_opt_our_(self):  # noqa
        with self._optional():
            self._stepper_series_()

    @tatsumasu()
    def _stepper_marker_(self):  # noqa
        self._S_()
        self._stepper_series_opt_our_()
        self.name_last_node('series')
        self._define(
            ['series'],
            []
        )

    @tatsumasu()
    def _permanent_t_(self):  # noqa
        self._permanent_marker_()
        self.name_last_node('type_marker')
        self._two_digit_number_()
        self.name_last_node('motor_body_length')
        self._stepper_suffix_t_()
        self.name_last_node('suffix')
        self._define(
            ['motor_body_length', 'suffix', 'type_marker'],
            []
        )

    @tatsumasu()
    def _brushless_marker_(self):  # noqa
        self._price_performance_or_unknown_C_marker_()
        self.name_last_node('is_price_performance')
        self._rounded_marker_()
        self.name_last_node('is_round')
        self._brushless_marker_base_()
        self._brushless_flat_marker_()
        self.name_last_node('is_flat')
        self._square_marker_()
        self.name_last_node('is_square')
        self._price_performance_or_unknown_C_marker_()
        self.name_last_node('is_unknown_C')
        self._define(
            ['is_flat', 'is_price_performance', 'is_round', 'is_square', 'is_unknown_C'],
            []
        )

    @tatsumasu()
    def _execution_configuration_t_(self):  # noqa
        self._Dash_()
        self._any_integer_()
        self.name_last_node('number')
        self._electrical_unit_()
        self.name_last_node('unit')
        self._define(
            ['number', 'unit'],
            []
        )

    @tatsumasu()
    def _brushless_modifier_variants_(self):  # noqa
        with self._choice():
            with self._option():
                self._brushless_modifier_poles_torque_()
                self.name_last_node('poles_torque')
                self._define(
                    ['poles_torque'],
                    []
                )
            with self._option():
                self._brushless_modifier_length_electronics_electrics_()
                self.name_last_node('length_electronics_electrics')
                self._define(
                    ['length_electronics_electrics'],
                    []
                )
            self._error(
                'expecting one of: '
                '<brushless_modifier_length_electronics_e'
                'lectrics>'
                '<brushless_modifier_poles_torque>'
                '<brushless_modifier_poles_torque_letter>'
                '<two_or_three_digit_number>'
            )
        self._define(
            ['length_electronics_electrics', 'poles_torque'],
            []
        )

    @tatsumasu()
    def _brushless_modifier_poles_torque_(self):  # noqa
        self._brushless_modifier_poles_torque_letter_()
        self.name_last_node('poles_or_other')
        self._two_digit_number_()
        self.name_last_node('variant')
        self._define(
            ['poles_or_other', 'variant'],
            []
        )

    @tatsumasu()
    def _brushless_modifier_length_electronics_electrics_(self):  # noqa
        self._two_or_three_digit_number_()
        self.name_last_node('motor_body_length')
        self._brushless_tail_opt_our_()
        self.name_last_node('tail')
        self._define(
            ['motor_body_length', 'tail'],
            []
        )

    @tatsumasu()
    def _brushless_tail_opt_our_(self):  # noqa
        with self._optional():
            self._brushless_tail_()

    @tatsumasu()
    def _brushless_t_(self):  # noqa
        self._brushless_marker_()
        self.name_last_node('type_marker')
        self._brushless_modifier_variants_()
        self.name_last_node('modifier')
        self._define(
            ['modifier', 'type_marker'],
            []
        )

    @tatsumasu()
    def _brushless_tail_(self):  # noqa
        with self._choice():
            with self._option():
                self._brushless_electronic_tail_()
                self.name_last_node('electronic')
                self._define(
                    ['electronic'],
                    []
                )
            with self._option():
                self._execution_configuration_t_()
                self.name_last_node('no_electronic')
                self._define(
                    ['no_electronic'],
                    []
                )
            self._error(
                'expecting one of: '
                '<Dash> <brushless_electronic_tail>'
                '<execution_configuration_t>'
                '<integrated_electronic_marker> [–-]'
            )
        self._define(
            ['electronic', 'no_electronic'],
            []
        )

    @tatsumasu()
    def _execution_configuration_opt_our_(self):  # noqa
        with self._optional():
            self._execution_configuration_t_()

    @tatsumasu()
    def _brushless_electronic_tail_(self):  # noqa
        self._integrated_electronic_marker_()
        self.name_last_node('has_electronics')
        self._execution_configuration_opt_our_()
        self.name_last_node('cfg')
        self._define(
            ['cfg', 'has_electronics'],
            []
        )

    @tatsumasu()
    def _digit_(self):  # noqa
        with self._choice():
            with self._option():
                self._RestOfDigits_()
            with self._option():
                self._Three_()
            self._error(
                'expecting one of: '
                "'3' <RestOfDigits> <Three> [0-24-9]"
            )

    @tatsumasu()
    def _square_marker_(self):  # noqa
        with self._optional():
            self._S_()

    @tatsumasu()
    def _stepper_series_(self):  # noqa
        with self._choice():
            with self._option():
                self._T_()
                self.name_last_node('standard')
                self._define(
                    ['standard'],
                    []
                )
            with self._option():
                self._H_()
                self.name_last_node('hybrid')
                self._define(
                    ['hybrid'],
                    []
                )
            self._error(
                'expecting one of: '
                "'H' 'T'"
            )
        self._define(
            ['hybrid', 'standard'],
            []
        )

    @tatsumasu()
    def _stepper_modifiers_t_(self):  # noqa
        with self._group():
            with self._choice():
                with self._option():
                    self._H_()
                with self._option():
                    self._C_()
                self._error(
                    'expecting one of: '
                    "'C' 'H'"
                )
        self.name_last_node('stepper_modifiers')
        self._define(
            ['stepper_modifiers'],
            []
        )

    @tatsumasu()
    def _price_performance_or_unknown_C_marker_(self):  # noqa
        with self._optional():
            self._C_()

    @tatsumasu()
    def _electrical_unit_(self):  # noqa
        with self._choice():
            with self._option():
                self._A_()
            with self._option():
                self._V_()
            self._error(
                'expecting one of: '
                "'A' 'V'"
            )

    @tatsumasu()
    def _shafts_count_marker_(self):  # noqa
        with self._choice():
            with self._option():
                self._A_()
            with self._option():
                self._B_()
            self._error(
                'expecting one of: '
                "'A' 'B'"
            )

    @tatsumasu()
    def _one_or_two_digit_number_(self):  # noqa
        self._digit_()
        with self._optional():
            self._digit_()

    @tatsumasu()
    def _two_digit_number_(self):  # noqa
        self._digit_()
        self._digit_()

    @tatsumasu()
    def _three_digit_number_(self):  # noqa
        self._two_digit_number_()
        self._digit_()

    @tatsumasu()
    def _two_or_three_digit_number_(self):  # noqa
        self._two_digit_number_()
        with self._optional():
            self._digit_()

    @tatsumasu()
    def _any_integer_(self):  # noqa

        def block0():
            self._digit_()
        self._positive_closure(block0)

    @tatsumasu()
    def _fractional_part_(self):  # noqa
        self._dot_()
        with self._optional():
            self._any_integer_()

    @tatsumasu()
    def _float_number_(self):  # noqa
        self._any_integer_()
        with self._optional():
            self._fractional_part_()

    @tatsumasu()
    def _integrated_electronic_marker_(self):  # noqa
        self._Dash_()
        self._I_()
        self._E_()

    @tatsumasu()
    def _brushless_modifier_poles_torque_letter_(self):  # noqa
        with self._choice():
            with self._option():
                self._A_()
            with self._option():
                self._B_()
            self._error(
                'expecting one of: '
                "'A' 'B'"
            )

    @tatsumasu()
    def _three_phase_marker_(self):  # noqa
        self._Three_()
        self._P_()

    @tatsumasu()
    def _hollow_specifier_(self):  # noqa
        self._Dash_()
        self._H_()

    @tatsumasu()
    def _Three_(self):  # noqa
        self._token('3')

    @tatsumasu()
    def _RestOfDigits_(self):  # noqa
        self._pattern('[0-24-9]')

    @tatsumasu()
    def _Dash_(self):  # noqa
        self._pattern('[–-]')

    @tatsumasu()
    def _dot_(self):  # noqa
        self._token('.')

    @tatsumasu()
    def _A_(self):  # noqa
        self._token('A')

    @tatsumasu()
    def _B_(self):  # noqa
        self._token('B')

    @tatsumasu()
    def _C_(self):  # noqa
        self._token('C')

    @tatsumasu()
    def _E_(self):  # noqa
        self._token('E')

    @tatsumasu()
    def _F_(self):  # noqa
        self._token('F')

    @tatsumasu()
    def _G_(self):  # noqa
        self._token('G')

    @tatsumasu()
    def _H_(self):  # noqa
        self._token('H')

    @tatsumasu()
    def _I_(self):  # noqa
        self._token('I')

    @tatsumasu()
    def _K_(self):  # noqa
        self._token('K')

    @tatsumasu()
    def _L_(self):  # noqa
        self._token('L')

    @tatsumasu()
    def _M_(self):  # noqa
        self._token('M')

    @tatsumasu()
    def _P_(self):  # noqa
        self._token('P')

    @tatsumasu()
    def _R_(self):  # noqa
        self._token('R')

    @tatsumasu()
    def _S_(self):  # noqa
        self._token('S')

    @tatsumasu()
    def _T_(self):  # noqa
        self._token('T')

    @tatsumasu()
    def _V_(self):  # noqa
        self._token('V')

    @tatsumasu()
    def _W_(self):  # noqa
        self._token('W')

    @tatsumasu()
    def _fl_(self):  # noqa
        self._F_()
        self._L_()

    @tatsumasu()
    def _permanent_marker_(self):  # noqa
        self._P_()
        self._M_()

    @tatsumasu()
    def _brushless_marker_base_(self):  # noqa
        self._B_()
        self._L_()

    @tatsumasu()
    def _rounded_marker_(self):  # noqa
        with self._optional():
            self._R_()

    @tatsumasu()
    def _brushless_flat_marker_(self):  # noqa
        with self._optional():
            self._W_()


class fulling_motor_nameSemantics:
    def main(self, ast):  # noqa
        return ast

    def gearbox_specifier(self, ast):  # noqa
        return ast

    def type_specific(self, ast):  # noqa
        return ast

    def three_phase_t(self, ast):  # noqa
        return ast

    def three_phase_suffix_opt_our(self, ast):  # noqa
        return ast

    def three_phase_suffix_t(self, ast):  # noqa
        return ast

    def stepper_suffix_t(self, ast):  # noqa
        return ast

    def suffix_with_or_without_tail(self, ast):  # noqa
        return ast

    def suffix_with_current(self, ast):  # noqa
        return ast

    def double_step_rate_marker(self, ast):  # noqa
        return ast

    def encoder_presence_marker(self, ast):  # noqa
        return ast

    def unknown_marker_F(self, ast):  # noqa
        return ast

    def keyway_marker(self, ast):  # noqa
        return ast

    def screwed_shaft_marker(self, ast):  # noqa
        return ast

    def gearbox_specifier_opt_our(self, ast):  # noqa
        return ast

    def hollow_specifier_opt_our(self, ast):  # noqa
        return ast

    def shafts_count_marker_opt_our(self, ast):  # noqa
        return ast

    def shafts_count_and_step_rate_any_order_1_t(self, ast):  # noqa
        return ast

    def shafts_count_and_step_rate_any_order_2_t(self, ast):  # noqa
        return ast

    def shafts_count_and_step_rate_any_order_t(self, ast):  # noqa
        return ast

    def stepper_suffix_tail(self, ast):  # noqa
        return ast

    def stepper_modifiers_opt_our(self, ast):  # noqa
        return ast

    def stepper_t(self, ast):  # noqa
        return ast

    def stepper_series_opt_our(self, ast):  # noqa
        return ast

    def stepper_marker(self, ast):  # noqa
        return ast

    def permanent_t(self, ast):  # noqa
        return ast

    def brushless_marker(self, ast):  # noqa
        return ast

    def execution_configuration_t(self, ast):  # noqa
        return ast

    def brushless_modifier_variants(self, ast):  # noqa
        return ast

    def brushless_modifier_poles_torque(self, ast):  # noqa
        return ast

    def brushless_modifier_length_electronics_electrics(self, ast):  # noqa
        return ast

    def brushless_tail_opt_our(self, ast):  # noqa
        return ast

    def brushless_t(self, ast):  # noqa
        return ast

    def brushless_tail(self, ast):  # noqa
        return ast

    def execution_configuration_opt_our(self, ast):  # noqa
        return ast

    def brushless_electronic_tail(self, ast):  # noqa
        return ast

    def digit(self, ast):  # noqa
        return ast

    def square_marker(self, ast):  # noqa
        return ast

    def stepper_series(self, ast):  # noqa
        return ast

    def stepper_modifiers_t(self, ast):  # noqa
        return ast

    def price_performance_or_unknown_C_marker(self, ast):  # noqa
        return ast

    def electrical_unit(self, ast):  # noqa
        return ast

    def shafts_count_marker(self, ast):  # noqa
        return ast

    def one_or_two_digit_number(self, ast):  # noqa
        return ast

    def two_digit_number(self, ast):  # noqa
        return ast

    def three_digit_number(self, ast):  # noqa
        return ast

    def two_or_three_digit_number(self, ast):  # noqa
        return ast

    def any_integer(self, ast):  # noqa
        return ast

    def fractional_part(self, ast):  # noqa
        return ast

    def float_number(self, ast):  # noqa
        return ast

    def integrated_electronic_marker(self, ast):  # noqa
        return ast

    def brushless_modifier_poles_torque_letter(self, ast):  # noqa
        return ast

    def three_phase_marker(self, ast):  # noqa
        return ast

    def hollow_specifier(self, ast):  # noqa
        return ast

    def Three(self, ast):  # noqa
        return ast

    def RestOfDigits(self, ast):  # noqa
        return ast

    def Dash(self, ast):  # noqa
        return ast

    def dot(self, ast):  # noqa
        return ast

    def A(self, ast):  # noqa
        return ast

    def B(self, ast):  # noqa
        return ast

    def C(self, ast):  # noqa
        return ast

    def E(self, ast):  # noqa
        return ast

    def F(self, ast):  # noqa
        return ast

    def G(self, ast):  # noqa
        return ast

    def H(self, ast):  # noqa
        return ast

    def I(self, ast):  # noqa
        return ast

    def K(self, ast):  # noqa
        return ast

    def L(self, ast):  # noqa
        return ast

    def M(self, ast):  # noqa
        return ast

    def P(self, ast):  # noqa
        return ast

    def R(self, ast):  # noqa
        return ast

    def S(self, ast):  # noqa
        return ast

    def T(self, ast):  # noqa
        return ast

    def V(self, ast):  # noqa
        return ast

    def W(self, ast):  # noqa
        return ast

    def fl(self, ast):  # noqa
        return ast

    def permanent_marker(self, ast):  # noqa
        return ast

    def brushless_marker_base(self, ast):  # noqa
        return ast

    def rounded_marker(self, ast):  # noqa
        return ast

    def brushless_flat_marker(self, ast):  # noqa
        return ast


def main(filename, start=None, **kwargs):
    if start is None:
        start = 'main'
    if not filename or filename == '-':
        text = sys.stdin.read()
    else:
        with open(filename) as f:
            text = f.read()
    parser = fulling_motor_nameParser()
    return parser.parse(
        text,
        rule_name=start,
        filename=filename,
        **kwargs
    )


if __name__ == '__main__':
    import json
    from tatsu.util import asjson

    ast = generic_main(main, fulling_motor_nameParser, name='fulling_motor_name')
    data = asjson(ast)
    print(json.dumps(data, indent=2))
