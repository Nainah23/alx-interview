# Star Wars Characters

This project involves writing a script that prints all characters from a specific Star Wars movie using the Star Wars API. The script takes a Movie ID as a positional argument and displays each character's name in the same order as they appear in the "characters" list from the /films/ endpoint.

## Usage

To run the script, use the following command:

```bash
./0-starwars_characters.js <Movie_ID>
```

- Replace `<Movie_ID>` with the ID of the Star Wars movie you want to query. For example, `3` corresponds to "Return of the Jedi".

### Example

```bash
./0-starwars_characters.js 3
```

This command will output:

```
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```

## Requirements

- The script must use the Star Wars API.
- The `requests` module must be used for making API calls.

## Repository Structure

- **GitHub repository:** `alx-interview`
- **Directory:** `0x06-starwars_api`
- **File:** `0-starwars_characters.js`

## Installation

Ensure you have Node.js and npm installed. Then, install the `request` module by running:

```bash
npm install request
```

## Notes

- Ensure that you have the necessary permissions to execute the script (`chmod +x 0-starwars_characters.js`).
- The script displays character names in the same order as the "characters" list from the Star Wars API `/films/` endpoint.
