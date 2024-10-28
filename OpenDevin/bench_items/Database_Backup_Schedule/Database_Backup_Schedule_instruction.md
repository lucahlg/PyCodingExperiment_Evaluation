# Modify and Optimize a Backup Configuration

## Objective:

The goal of this exercise is to modify and optimize a JSON object representing a database backup configuration. You will be asked to update settings for frequency, retention, and data export options.

## Exercise Instructions:

You are provided with a JSON file defining the parameters for a database backup process. Your tasks are as follows:

1. **Increase Backup Frequency:** Change the "backupPolicy.count" value to 7, indicating that backups should be performed weekly.
2. **Extend Data Retention:** Update the "backupPolicy.retentionPeriodDays" to 60 days, extending the period for which backup data is retained.
3. **Modify Export Compression:** Change the "exportOptions.fileCompressionSource" from "GCS" to "ZIP," compressing exported backup files in ZIP format.
4.  **Update Description:** Modify the "description" field to accurately reflect the updated backup settings: "Weekly Backup with 60-Day Retention and ZIP Compression".



