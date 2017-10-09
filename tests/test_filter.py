# -*- coding: utf-8 -*-

import pytest
from filters.filter import *

@pytest.fixture(scope = 'session')
def filter_one():
	return filter(alias='filtro', ip='192.168.2.1', method=['GET', 'POST'])

@pytest.fixture(scope = 'session')
def filter_two():
	return filter(alias='filtro', ip='192.168.2.1', method='GET', uri=['example-01', 'example-03'])

@pytest.fixture(scope = 'session')
def filter_three():
	return filter(alias='filtro', equals=True, ip='192.168.2.1', method='GET', uri=['example-01', 'example-03'])

class Test_Filter_1(object):
	def test_one(self, filter_one):
		boolean = filter_one.check_filter(ip='192.168.2.1', method='GET')
		assert boolean == True
	def test_two(self, filter_one):
		boolean = filter_one.check_filter(ip='192.168.2.1', method='POST')
		assert boolean == True
	def test_three(self, filter_one):
		boolean = filter_one.check_filter(ip='192.168.2.1', method='GET', uri='EXAMPLE')
		assert boolean == True
	def test_four(self, filter_one):
		boolean = filter_one.check_filter(ip='192.168.2.1', method='GET', uri='EXAMPLE', potato='potato')
		assert boolean == True
	def test_five(self, filter_one):
		boolean = filter_one.check_filter(ip='192.168.2.2', method='GET')
		assert boolean == False
	def test_six(self, filter_one):
		boolean = filter_one.check_filter(ip='192.168.2.1', method='POTATO')
		assert boolean == False
	def test_seven(self, filter_one):
		boolean = filter_one.check_filter()
		assert boolean == False
	def test_eight(self, filter_one):
		boolean = filter_one.check_filter(potato='potato')
		assert boolean == False

class Test_Filter_2(object):
	def test_one(self, filter_two):
		boolean = filter_two.check_filter(ip='192.168.2.1', method='GET', uri='-abasda-example-01-abasda')
		assert boolean == True
	def test_two(self, filter_two):
		boolean = filter_two.check_filter(ip='192.168.2.1', method='GET', uri='EXAMPLE')
		assert boolean == False
	def test_three(self, filter_two):
		boolean = filter_two.check_filter(ip='192.168.2.1', method='GET', uri='EXAMPLE', patata='patata')
		assert boolean == False
	def test_four(self, filter_two):
		boolean = filter_two.check_filter(ip='192.168.2.1', method='GET', uri='abasda-example-02-abasda')
		assert boolean == False
	def test_five(self, filter_two):
		boolean = filter_two.check_filter(ip='192.168.2.1', method='POST')
		assert boolean == False
	def test_six(self, filter_two):
		boolean = filter_two.check_filter(ip='192.168.2.2', method='GET')
		assert boolean == False
	def test_seven(self, filter_two):
		boolean = filter_two.check_filter()
		assert boolean == False
	def test_eight(self, filter_two):
		boolean = filter_two.check_filter(ip='192.168.2.1', method='GET', uri='-abasda-example-03-abasda')
		assert boolean == True
	def test_nine(self, filter_two):
		boolean = filter_two.check_filter(potato='potato')
		assert boolean == False


class Test_Filter_2(object):
	def test_one(self, filter_three):
		boolean = filter_three.check_filter(ip='192.168.2.1', method='GET', uri='-abasda-example-01-abasda')
		assert boolean == False
	def test_two(self, filter_three):
		boolean = filter_three.check_filter(ip='192.168.2.1', method='GET', uri='EXAMPLE')
		assert boolean == False
	def test_three(self, filter_three):
		boolean = filter_three.check_filter(ip='192.168.2.1', method='GET', uri='EXAMPLE', patata='patata')
		assert boolean == False
	def test_four(self, filter_three):
		boolean = filter_three.check_filter(ip='192.168.2.1', method='GET', uri='abasda-example-02-abasda')
		assert boolean == False
	def test_five(self, filter_three):
		boolean = filter_three.check_filter(ip='192.168.2.1', method='POST')
		assert boolean == False
	def test_six(self, filter_three):
		boolean = filter_three.check_filter(ip='192.168.2.2', method='GET')
		assert boolean == False
	def test_seven(self, filter_three):
		boolean = filter_three.check_filter()
		assert boolean == False
	def test_eight(self, filter_three):
		boolean = filter_three.check_filter(ip='192.168.2.1', method='GET', uri='-abasda-example-03-abasda')
		assert boolean == False
	def test_nine(self, filter_three):
		boolean = filter_three.check_filter(ip='192.168.2.1', method='GET', uri='example-03')
		assert boolean == True
	def test_nine(self, filter_three):
		boolean = filter_three.check_filter(ip='192.168.2.1', method='GET', uri='example-01')
		assert boolean == True
	def test_ten(self, filter_three):
		boolean = filter_three.check_filter(potato='potato')
		assert boolean == False

