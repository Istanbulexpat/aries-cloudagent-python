"""Base holder class."""

from abc import ABC, ABCMeta, abstractmethod
from typing import Union


class BaseHolder(ABC, metaclass=ABCMeta):
    """Base class for holder."""

    def __repr__(self) -> str:
        """
        Return a human readable representation of this class.

        Returns:
            A human readable string for this class

        """
        return "<{}>".format(self.__class__.__name__)

    @abstractmethod
    async def get_credential(self, credential_id: str):
        """
        Get a credential stored in the wallet.

        Args:
            credential_id: Credential id to retrieve

        """

    @abstractmethod
    async def delete_credential(self, credential_id: str):
        """
        Remove a credential stored in the wallet.

        Args:
            credential_id: Credential id to remove

        """

    @abstractmethod
    async def get_mime_type(
        self, credential_id: str, attr: str = None
    ) -> Union[dict, str]:
        """
        Get MIME type per attribute (or for all attributes).

        Args:
            credential_id: credential id
            attr: attribute of interest or omit for all

        Returns: Attribute MIME type or dict mapping attribute names to MIME types
            attr_meta_json = all_meta.tags.get(attr)

        """

    @abstractmethod
    async def create_presentation(
        self,
        presentation_request: dict,
        requested_credentials: dict,
        schemas: dict,
        credential_definitions: dict,
        rev_states_json: dict = None,
    ):
        """
        Get credentials stored in the wallet.

        Args:
            presentation_request: Valid indy format presentation request
            requested_credentials: Indy format requested_credentials
            schemas: Indy formatted schemas_json
            credential_definitions: Indy formatted schemas_json
            rev_states_json: Indy format revocation states
        """

    @abstractmethod
    async def create_credential_request(
        self, credential_offer, credential_definition, holder_did: str
    ):
        """
        Create a credential offer for the given credential definition id.

        Args:
            credential_offer: The credential offer to create request for
            credential_definition: The credential definition to create an offer for
            holder_did: the DID of the agent making the request

        Returns:
            A credential request

        """

    @abstractmethod
    async def store_credential(
        self,
        credential_definition,
        credential_data,
        credential_request_metadata,
        credential_attr_mime_types=None,
        credential_id=None,
        rev_reg_def_json=None,
    ):
        """
        Store a credential in the wallet.

        Args:
            credential_definition: Credential definition for this credential
            credential_data: Credential data generated by the issuer
            credential_request_metadata: credential request metadata generated
                by the issuer
            credential_attr_mime_types: dict mapping attribute names to (optional)
                MIME types to store as non-secret record, if specified
            credential_id: optionally override the stored credential id
            rev_reg_def_json: optional revocation registry definition in json

        """
