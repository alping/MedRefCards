# MedRefCards - Medical reference cards

Swe: Ett projekt som syftar till att skapa referenskort som kan användas inom hälso- och sjukvård.

OBSERVERA ATT DETTA ÄR ETT PROJEKT UNDER ARBETE OCH ATT ALL ANVÄNDNING SKER PÅ EGET ANSVAR. INGEN GARANTI KAN GES FÖR ATT DEN INFORMATION SOM FINNS HÄR ÄR KORREKT ELLER UPPDATERAD.

Eng: A project to create a series of reference cards, usable to anyone involved in health care and medicine.

PLEASE BE AWARE THAT THIS IS VERY MUCH A WORK IN PROGRESS AND THUS NO GUARANTEE FOR THE CORRECTNESS OR COMPLETENESS OF THESE CARDS CAN BE GIVEN. USE THESE CARDS AT YOUR OWN RISK.

## Usage
This is a collection of reference cards for the use in medical practice. These cards are designed to be printed, folded, laminated, and put on a key ring, or to be viewed on a screen, of for example a phone or a tablet.

The cards can either be downloaded directly from the [pdf folder](pdf "pdf folder") in this repository, or built from source using the python script `medical-reference-cards.py` in the [scripts folder](scripts "scripts folder").

## Brief instructions for contributors
Contributing is easy! You just need to create one pdf file for the front and one for the back of the card (you can use the [Word template](templates/word-content-template.dotx "Word template")), and then fill in some information in a [text file](templates/card-description-template.yml "Card description template") (see also the [example below](#structure-of-yml-file)), and then your done! Well almost, you also have to submit your new cards to the repository, either by sending me an email or by using git (for the computer savvy). Thank you for your contribution!

## Detailed instructions for contributors

### The building blocks of a card
- Each card has a front and back face.
- Each face has a coloured frame, a heading, a content area, and a footer
- The dimensions of a folded card are 105mm x 150mm
- The dimensions of the content area are 100mm x 130mm
- The meta-data for each card are stored in a .yaml file
- The content for each card is stored in a separate pdf file for each face
- The cards are outputted to a pdf file by running the python script `MedRefCards.py`

### Files and naming convention
There are 3 files making up each card (replace `card` with actual card name and `domain` with actual domain name):
+ `domain-card.yaml`
+ `domain-card-front.pdf`
+ `domain-card-back.pdf`

Besides these files, there might be additional source files (files containing data or designs) for each card located in the source subfolder.

For filenames use:
  - The domain and card name as the base
  - All lowercase letters
  - Hyphens (-) to combine words
  - Example filenames for card describing the normal physiology for the pediatrics domain:
    + `pediatrics-normal-physiology.yaml`
    + `pediatrics-normal-physiology_front.pdf`
    + `pediatrics-normal-physiology_back.pdf`

### Style guide for content
- Font: Arial or Helvetica, around 10p (depending on content)
- Images: Preferably vector images

### Structure of .yml file
```yaml
## Card ########################
domain: 'Domain Name'
category: 'Category Name'

modified_date: 'Date of last modification'
verified_date: 'Date of verification'
verified_by: 'Verified by'

## Front #######################
front_header: 'Header of front face'
front_footer: 'Footer of front face'

front_toc:
  - 'Table of contents for front face'
  - 'As a list'
front_references:
  - 'References for front face'
  - 'As a list'

## Back ########################
back_header: 'Header of back face'
back_footer: 'Footer of back face'

back_toc:
  - 'Table of contents for front face'
  - 'As a list'
back_references:
  - 'References for back face'
  - 'As a list'
```
For more info on YAML, see http://yaml.org/

### Dimension of content .pdf files
- The dimensions should be 100mm x 130mm (width x height)

## Contributors
- Peter Alping (contact@alping.se) - Medical student, Karolinska Institutet, Sweden
- Sebastian Samuelsson - Medical student, Karolinska Institutet, Sweden
- Martin Östholm - Medical student, Karolinska Institutet, Sweden
- Marius Matusevicius - Medical student, Karolinska Institutet, Sweden
- Kajsa Thilander - Medical student, Karolinska Institutet, Sweden
- Emil Sternegård - Medical student, Karolinska Institutet, Sweden