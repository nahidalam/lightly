# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@lightly.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from lightly.openapi_generated.swagger_client.configuration import Configuration


class DockerRunScheduledData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'MongoObjectID',
        'dataset_id': 'MongoObjectID',
        'config_id': 'MongoObjectID',
        'priority': 'DockerRunScheduledPriority',
        'state': 'DockerRunScheduledState',
        'created_at': 'Timestamp',
        'last_modified_at': 'Timestamp',
        'owner': 'MongoObjectID'
    }

    attribute_map = {
        'id': 'id',
        'dataset_id': 'datasetId',
        'config_id': 'configId',
        'priority': 'priority',
        'state': 'state',
        'created_at': 'createdAt',
        'last_modified_at': 'lastModifiedAt',
        'owner': 'owner'
    }

    def __init__(self, id=None, dataset_id=None, config_id=None, priority=None, state=None, created_at=None, last_modified_at=None, owner=None, _configuration=None):  # noqa: E501
        """DockerRunScheduledData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._dataset_id = None
        self._config_id = None
        self._priority = None
        self._state = None
        self._created_at = None
        self._last_modified_at = None
        self._owner = None
        self.discriminator = None

        self.id = id
        self.dataset_id = dataset_id
        self.config_id = config_id
        self.priority = priority
        self.state = state
        self.created_at = created_at
        self.last_modified_at = last_modified_at
        if owner is not None:
            self.owner = owner

    @property
    def id(self):
        """Gets the id of this DockerRunScheduledData.  # noqa: E501


        :return: The id of this DockerRunScheduledData.  # noqa: E501
        :rtype: MongoObjectID
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DockerRunScheduledData.


        :param id: The id of this DockerRunScheduledData.  # noqa: E501
        :type: MongoObjectID
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def dataset_id(self):
        """Gets the dataset_id of this DockerRunScheduledData.  # noqa: E501


        :return: The dataset_id of this DockerRunScheduledData.  # noqa: E501
        :rtype: MongoObjectID
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this DockerRunScheduledData.


        :param dataset_id: The dataset_id of this DockerRunScheduledData.  # noqa: E501
        :type: MongoObjectID
        """
        if self._configuration.client_side_validation and dataset_id is None:
            raise ValueError("Invalid value for `dataset_id`, must not be `None`")  # noqa: E501

        self._dataset_id = dataset_id

    @property
    def config_id(self):
        """Gets the config_id of this DockerRunScheduledData.  # noqa: E501


        :return: The config_id of this DockerRunScheduledData.  # noqa: E501
        :rtype: MongoObjectID
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        """Sets the config_id of this DockerRunScheduledData.


        :param config_id: The config_id of this DockerRunScheduledData.  # noqa: E501
        :type: MongoObjectID
        """
        if self._configuration.client_side_validation and config_id is None:
            raise ValueError("Invalid value for `config_id`, must not be `None`")  # noqa: E501

        self._config_id = config_id

    @property
    def priority(self):
        """Gets the priority of this DockerRunScheduledData.  # noqa: E501


        :return: The priority of this DockerRunScheduledData.  # noqa: E501
        :rtype: DockerRunScheduledPriority
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this DockerRunScheduledData.


        :param priority: The priority of this DockerRunScheduledData.  # noqa: E501
        :type: DockerRunScheduledPriority
        """
        if self._configuration.client_side_validation and priority is None:
            raise ValueError("Invalid value for `priority`, must not be `None`")  # noqa: E501

        self._priority = priority

    @property
    def state(self):
        """Gets the state of this DockerRunScheduledData.  # noqa: E501


        :return: The state of this DockerRunScheduledData.  # noqa: E501
        :rtype: DockerRunScheduledState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DockerRunScheduledData.


        :param state: The state of this DockerRunScheduledData.  # noqa: E501
        :type: DockerRunScheduledState
        """
        if self._configuration.client_side_validation and state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def created_at(self):
        """Gets the created_at of this DockerRunScheduledData.  # noqa: E501


        :return: The created_at of this DockerRunScheduledData.  # noqa: E501
        :rtype: Timestamp
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DockerRunScheduledData.


        :param created_at: The created_at of this DockerRunScheduledData.  # noqa: E501
        :type: Timestamp
        """
        if self._configuration.client_side_validation and created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def last_modified_at(self):
        """Gets the last_modified_at of this DockerRunScheduledData.  # noqa: E501


        :return: The last_modified_at of this DockerRunScheduledData.  # noqa: E501
        :rtype: Timestamp
        """
        return self._last_modified_at

    @last_modified_at.setter
    def last_modified_at(self, last_modified_at):
        """Sets the last_modified_at of this DockerRunScheduledData.


        :param last_modified_at: The last_modified_at of this DockerRunScheduledData.  # noqa: E501
        :type: Timestamp
        """
        if self._configuration.client_side_validation and last_modified_at is None:
            raise ValueError("Invalid value for `last_modified_at`, must not be `None`")  # noqa: E501

        self._last_modified_at = last_modified_at

    @property
    def owner(self):
        """Gets the owner of this DockerRunScheduledData.  # noqa: E501


        :return: The owner of this DockerRunScheduledData.  # noqa: E501
        :rtype: MongoObjectID
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this DockerRunScheduledData.


        :param owner: The owner of this DockerRunScheduledData.  # noqa: E501
        :type: MongoObjectID
        """

        self._owner = owner

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(DockerRunScheduledData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DockerRunScheduledData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DockerRunScheduledData):
            return True

        return self.to_dict() != other.to_dict()
