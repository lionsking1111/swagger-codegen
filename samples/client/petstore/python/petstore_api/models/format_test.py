# coding: utf-8

"""
    Swagger Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class FormatTest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, integer=None, int32=None, int64=None, number=None, float=None, double=None, string=None, byte=None, binary=None, date=None, date_time=None, uuid=None, password=None):
        """
        FormatTest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'integer': 'int',
            'int32': 'int',
            'int64': 'int',
            'number': 'float',
            'float': 'float',
            'double': 'float',
            'string': 'str',
            'byte': 'str',
            'binary': 'str',
            'date': 'date',
            'date_time': 'datetime',
            'uuid': 'str',
            'password': 'str'
        }

        self.attribute_map = {
            'integer': 'integer',
            'int32': 'int32',
            'int64': 'int64',
            'number': 'number',
            'float': 'float',
            'double': 'double',
            'string': 'string',
            'byte': 'byte',
            'binary': 'binary',
            'date': 'date',
            'date_time': 'dateTime',
            'uuid': 'uuid',
            'password': 'password'
        }

        self._integer = integer
        self._int32 = int32
        self._int64 = int64
        self._number = number
        self._float = float
        self._double = double
        self._string = string
        self._byte = byte
        self._binary = binary
        self._date = date
        self._date_time = date_time
        self._uuid = uuid
        self._password = password


    @property
    def integer(self):
        """
        Gets the integer of this FormatTest.


        :return: The integer of this FormatTest.
        :rtype: int
        """
        return self._integer

    @integer.setter
    def integer(self, integer):
        """
        Sets the integer of this FormatTest.


        :param integer: The integer of this FormatTest.
        :type: int
        """

        if not integer:
            raise ValueError("Invalid value for `integer`, must not be `None`")
        if integer > 100.0:
            raise ValueError("Invalid value for `integer`, must be a value less than or equal to `100.0`")
        if integer < 10.0:
            raise ValueError("Invalid value for `integer`, must be a value greater than or equal to `10.0`")

        self._integer = integer

    @property
    def int32(self):
        """
        Gets the int32 of this FormatTest.


        :return: The int32 of this FormatTest.
        :rtype: int
        """
        return self._int32

    @int32.setter
    def int32(self, int32):
        """
        Sets the int32 of this FormatTest.


        :param int32: The int32 of this FormatTest.
        :type: int
        """

        if not int32:
            raise ValueError("Invalid value for `int32`, must not be `None`")
        if int32 > 200.0:
            raise ValueError("Invalid value for `int32`, must be a value less than or equal to `200.0`")
        if int32 < 20.0:
            raise ValueError("Invalid value for `int32`, must be a value greater than or equal to `20.0`")

        self._int32 = int32

    @property
    def int64(self):
        """
        Gets the int64 of this FormatTest.


        :return: The int64 of this FormatTest.
        :rtype: int
        """
        return self._int64

    @int64.setter
    def int64(self, int64):
        """
        Sets the int64 of this FormatTest.


        :param int64: The int64 of this FormatTest.
        :type: int
        """

        self._int64 = int64

    @property
    def number(self):
        """
        Gets the number of this FormatTest.


        :return: The number of this FormatTest.
        :rtype: float
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this FormatTest.


        :param number: The number of this FormatTest.
        :type: float
        """

        if not number:
            raise ValueError("Invalid value for `number`, must not be `None`")
        if number > 543.2:
            raise ValueError("Invalid value for `number`, must be a value less than or equal to `543.2`")
        if number < 32.1:
            raise ValueError("Invalid value for `number`, must be a value greater than or equal to `32.1`")

        self._number = number

    @property
    def float(self):
        """
        Gets the float of this FormatTest.


        :return: The float of this FormatTest.
        :rtype: float
        """
        return self._float

    @float.setter
    def float(self, float):
        """
        Sets the float of this FormatTest.


        :param float: The float of this FormatTest.
        :type: float
        """

        if not float:
            raise ValueError("Invalid value for `float`, must not be `None`")
        if float > 987.6:
            raise ValueError("Invalid value for `float`, must be a value less than or equal to `987.6`")
        if float < 54.3:
            raise ValueError("Invalid value for `float`, must be a value greater than or equal to `54.3`")

        self._float = float

    @property
    def double(self):
        """
        Gets the double of this FormatTest.


        :return: The double of this FormatTest.
        :rtype: float
        """
        return self._double

    @double.setter
    def double(self, double):
        """
        Sets the double of this FormatTest.


        :param double: The double of this FormatTest.
        :type: float
        """

        if not double:
            raise ValueError("Invalid value for `double`, must not be `None`")
        if double > 123.4:
            raise ValueError("Invalid value for `double`, must be a value less than or equal to `123.4`")
        if double < 67.8:
            raise ValueError("Invalid value for `double`, must be a value greater than or equal to `67.8`")

        self._double = double

    @property
    def string(self):
        """
        Gets the string of this FormatTest.


        :return: The string of this FormatTest.
        :rtype: str
        """
        return self._string

    @string.setter
    def string(self, string):
        """
        Sets the string of this FormatTest.


        :param string: The string of this FormatTest.
        :type: str
        """

        if not string:
            raise ValueError("Invalid value for `string`, must not be `None`")
        if not re.search('[a-z]', string, flags=re.IGNORECASE):
            raise ValueError("Invalid value for `string`, must be a follow pattern or equal to `/[a-z]/i`")

        self._string = string

    @property
    def byte(self):
        """
        Gets the byte of this FormatTest.


        :return: The byte of this FormatTest.
        :rtype: str
        """
        return self._byte

    @byte.setter
    def byte(self, byte):
        """
        Sets the byte of this FormatTest.


        :param byte: The byte of this FormatTest.
        :type: str
        """

        self._byte = byte

    @property
    def binary(self):
        """
        Gets the binary of this FormatTest.


        :return: The binary of this FormatTest.
        :rtype: str
        """
        return self._binary

    @binary.setter
    def binary(self, binary):
        """
        Sets the binary of this FormatTest.


        :param binary: The binary of this FormatTest.
        :type: str
        """

        self._binary = binary

    @property
    def date(self):
        """
        Gets the date of this FormatTest.


        :return: The date of this FormatTest.
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this FormatTest.


        :param date: The date of this FormatTest.
        :type: date
        """

        self._date = date

    @property
    def date_time(self):
        """
        Gets the date_time of this FormatTest.


        :return: The date_time of this FormatTest.
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """
        Sets the date_time of this FormatTest.


        :param date_time: The date_time of this FormatTest.
        :type: datetime
        """

        self._date_time = date_time

    @property
    def uuid(self):
        """
        Gets the uuid of this FormatTest.


        :return: The uuid of this FormatTest.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this FormatTest.


        :param uuid: The uuid of this FormatTest.
        :type: str
        """

        self._uuid = uuid

    @property
    def password(self):
        """
        Gets the password of this FormatTest.


        :return: The password of this FormatTest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this FormatTest.


        :param password: The password of this FormatTest.
        :type: str
        """

        if not password:
            raise ValueError("Invalid value for `password`, must not be `None`")
        if len(password) > 64:
            raise ValueError("Invalid value for `password`, length must be less than or equal to `64`")
        if len(password) < 10:
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `10`")

        self._password = password

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
