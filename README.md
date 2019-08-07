# Problem #1: The Basics/ String/ Dictionary

## Given

A string as the following: 

> I completed **{number_of_sessions}** sessions and I rated my expert **{number_of_stars}** stars

while:
- `number_of_sessions` is any number in `[0, 1, ...9]`
- `number_of_stars` is any text in `[one, two, three, four, five]`

## Then

- Convert `number_of_sessions` from number to text.
- Convert `number_of_stars` from text to number.
- Using dictionaries and string methods.

## Expected output

For example, with `number_of_sessions` = `2` and `number_of_stars` = `five`, the original string will be:

> I completed **2** sessions and I rated my expert **five** stars

The result after conversion:

> I completed **two** sessions and I rated my expert **5** stars


# Problem #2: Object-Oriented Programming/ Exceptions

## Given

- Problem #1.

## Then

- Create a class `Step`:
  - `Step(number_of_sessions: int, number_of_stars: string)`
  - `make_step()`
- Create a class `Session` in `enums`:
  - `NUMBER_TO_TEXT_MAP`
  - `TEXT_TO_NUMBER_MAP`
- Create a class `InvalidValueException`:
  - `message`

- Move your code logic into the method `make_step()`. 
  
  Then you should be able to call your method as `Step(2, 'five').make_step()`.

- Move your dictionary maps into a class `Session` in a module called `enums`.
  
  It should be accessible via `enums.Session`.
  
  Remember update your `make_step` to use the enums.

- Create an exception `InvalidValueException` extends from `Exception`.

  It takes a message as the following: `InvalidValueException('Invalid number of sessions')`.

- When `Step` be created with invalid parameter(s), it should throw an `InvalidValueException` exception. 
  
  Try to catch and print out the message.

## Expected output

- `Step`, `Session` and `Exception` should have their own modules.
- Expected result:
  ```
  Step(2, 'five').make_step()
  > I completed two sessions and I rated my expert 5 stars
  ```

  ```
  Step(0, 'five').make_step()
  > Invalid number of sessions
  ```

  ```
  Step(2, 'ten').make_step()
  > Invalid number of stars
  ```


# Problem #3: Advanced Data Types

## Given

A list, a tuple and a set of numbers:
```
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = (3, 4, 1, 2, 7, 6, 5, 8)
c = {5, 6, 7, 8, 1, 2, 3, 4}
```

## Then

- Decide if `a`, `b`, `c` contain the same set of numbers.


## Expected output

The result should be `true`.


# Problem #4: Files/ JSON/ Dictionary/ Algorithm

## Given

A file `data.json` with the following content:

```json
{
  "expiration_time": 300,
  "id": 0,
  "product": "xchat",
  "storefront": {
      "banner_enabled": true,
      "banner_text": "Dynamic offer banner",
      "description": "",
      "enabled": true,
      "purchase_options": [
          {
              "button_text": "Dynamic offer - button_text",
              "description": "Dynamic offer - description",
              "id": "",
              "price": "7.99",
              "price_text": "price_text",
              "session_count": "3",
              "subtitle": "Dynamic offer - subtitle",
              "title": "Dynamic offer - title",
              "suffix": "Dynamic offer - suffix",
              "trial_duration": 0,
              "min_member_count": 1,
              "max_member_count": 1,
              "action": "purchase",
              "frequency_view": "monthly",
              "free_learning_subscription": false,
              "team_type": "personal",
              "frequency": null,
          }
      ],
  },
  "utm_campaign": "19203420349",
  "utm_source": "",
}
```

An object `modify_data` with the following content:

```python
modify_data = {
  "expiration_time": 200,
  "product": "qchat",
  "utm_campaign": str(time.time()),
  "storefront": {
    "banner_enabled": False,
    "purchase_options": [
          {
              "button_text": "Dynamic offer 1 - button_text",
              "description": "Dynamic offer 1 - description",
              "id": "",
              "price": "99.99",
              "price_text": "price_text",
              "session_count": "0",
              "subtitle": "Dynamic offer - subtitle",
              "title": "Dynamic offer - title",
              "suffix": "Dynamic offer - suffix",
              "trial_duration": 0,
              "min_member_count": 1,
              "max_member_count": 1,
              "action": "purchase",
              "frequency_view": "monthly",
              "free_learning_subscription": False,
              "team_type": "personal",
              "frequency": None,
          }
      ]
  }
}

```

## Then

- Create class model entities `StorefrontConfig`:
  - `StorefrontConfig(data: object)`
  - `update(modify_data: object)`: Write an algorithm to update data of the object using the dictionary provided (**not using direct variable assignment**).
- Create class `FileController`: 
  - `read_file(file_name): StorefrontConfig`.
  - `write_file(object: StorefrontConfig, file_name)`.
- The result should be written to file `result.json`.

## Expected output

```
file_controller = FileController()
config = file_controller.read_file("data.json")
config.update(modify_data)
file_controller.write_file(config, "result.json")
```

A new file `result.json` should be created with the following content:

```json
{
    "expiration_time": 200,
    "id": 0,
    "product": "qchat",
    "storefront": {
        "banner_enabled": false,
        "purchase_options": [
            {
                "button_text": "Dynamic offer 1 - button_text",
                "description": "Dynamic offer 1 - description",
                "id": "",
                "price": "99.99",
                "price_text": "price_text",
                "session_count": "0",
                "subtitle": "Dynamic offer - subtitle",
                "title": "Dynamic offer - title",
                "suffix": "Dynamic offer - suffix",
                "trial_duration": 0,
                "min_member_count": 1,
                "max_member_count": 1,
                "action": "purchase",
                "frequency_view": "monthly",
                "free_learning_subscription": false,
                "team_type": "personal",
                "frequency": null
            }
        ]
    },
    "utm_campaign": "updated_timestamp",
    "utm_source": ""
}
```

