
export class Form {
    description: string;
    creation_date: string;
    approximate_expiration_date: string;
    quality: string;
    manipulation: string;
  
    constructor(description: string, creation_date: string, approximate_expiration_date: string, quality: string, manipulation: string) {
      this.description = description;
      this.creation_date = creation_date;
      this.approximate_expiration_date = approximate_expiration_date;
      this.quality = quality;
      this.manipulation = manipulation;
    }

}