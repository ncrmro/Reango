from graphene import ObjectType, String, Union, Connection, Interface, Field


class TokensSuccess(ObjectType):
    """Returns token when used during signup, login"""
    token = String()


class TokenError(ObjectType):
    """Error returned when"""
    error = String()


class TokenUnion(Union):
    """Returns either token error or token success"""
    class Meta:
        types = (TokensSuccess, TokenError)


class TokenConnection(Connection):
    class Meta:
        node = TokenUnion


class TokensInterface(Interface):
    tokens = Field(TokenUnion)
