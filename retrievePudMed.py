from Bio import Entrez

# needed as per enterez documentation
Entrez.email = "sohankureti@gmail.com"


def fetch_pubmed_article_details():
    while True:  # Infinite loop to keep prompting for a valid PubMed ID
        try:
            # Prompt for PubMed ID input
            pubmed_id = input("What PubMed ID would you like to look up? ")

            # Fetch the paper details from PubMed using Entrez efetch
            handle = Entrez.efetch(db="pubmed", id=pubmed_id, retmode="xml")
            records = Entrez.read(handle)
            handle.close()

            # Extract the title and abstract
            article_title = records["PubmedArticle"][0]["MedlineCitation"]["Article"][
                "ArticleTitle"
            ]
            article_abstract = records["PubmedArticle"][0]["MedlineCitation"][
                "Article"
            ]["Abstract"]["AbstractText"][0]

            # Print the title and abstract
            print(f"Title: {article_title}\n")
            print(f"Abstract: {article_abstract}\n")
            break  # Exits the loop when successful

        except Exception as e:
            print("An error has occurred. Please try again.\n")


# Start the program
fetch_pubmed_article_details()
